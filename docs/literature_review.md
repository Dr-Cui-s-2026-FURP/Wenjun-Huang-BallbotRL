# Literature Review: Reinforcement Learning for Robotic Balance Control

**Project**: RL Balance & Roll - Ballbot Control  
**Date**: 2026-04-02  
**Author**: Wenjun Huang

---

## 📚 I. Paper Summary

| # | Paper | Core Contribution |
|---|-------|-------------------|
| 1 | Schulman et al., "Proximal Policy Optimization Algorithms" (2017) | PPO algorithm balancing TRPO's stability with implementation simplicity | 
| 2 | Hwangbo et al., "Learning Agile and Dynamic Motor Skills for Legged Robots" (Science Robotics 2019) | Successful sim-to-real transfer for ANYmal quadruped |
| 3 | Tobin et al., "Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World" (2017) | Foundational work on Domain Randomization | 
| 4 | OpenAI et al., "Learning Dexterous In-Hand Manipulation" (2018) | Large-scale distributed training for Shadow Hand dexterous manipulation |

---

## II. Core Algorithm: Proximal Policy Optimization (PPO)

### 2.1 Limitations of Traditional Policy Gradients

The standard policy gradient objective is:

$$L^{PG}(\theta) = \hat{\mathbb{E}}_t[\log \pi_\theta(a_t|s_t) \hat{A}_t]$$

The problem: performing multiple gradient updates on the same trajectory leads to **destructively large policy updates**. TRPO solves this with a KL divergence constraint, but it is complex to implement and incompatible with architectures that include noise.

### 2.2 PPO's Key Innovation: Clipped Surrogate Objective

PPO proposes a simpler solution — **clipping the probability ratio**:

$$L^{CLIP}(\theta) = \hat{\mathbb{E}}_t[\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]$$

where $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{\theta_{\text{old}}}(a_t|s_t)}$ is the probability ratio between new and old policies.

**Key insights**:
- When advantage $\hat{A}_t > 0$: clip only when $r_t > 1+\epsilon$ (prevents over-increasing probability of good actions)
- When advantage $\hat{A}_t < 0$: clip only when $r_t < 1-\epsilon$ (prevents over-decreasing probability of bad actions)
- The final objective forms a **pessimistic lower bound** on $L^{CPI}$, ensuring stable updates

### 2.3 Why PPO is Suitable for Robot Control

| Property | Significance for Robot Control |
|----------|-------------------------------|
| Multiple epochs per update | Improved sample efficiency, reduces real robot interaction |
| Clipping mechanism | Prevents catastrophic forgetting, ensures hardware safety |
| First-order optimization | Simple implementation, easy to debug |
| LSTM compatibility | Handles partial observability (e.g., contact states) |

---

## III. Domain Randomization: Bridging the Sim2Real Gap

### 3.1 What is the Reality Gap?

Discrepancies between simulation and the real world arise from:

- **Physical parameters**: friction, mass, stiffness
- **Actuators**: latency, dead zones, nonlinearities
- **Sensors**: noise, dropped frames, calibration errors
- **Environment**: lighting, textures, occlusions

Tobin et al.'s core hypothesis: **If the variability in simulation is significant enough, the real world appears as just another variation.**

### 3.2 Domain Randomization Principle

Randomize simulation parameters during training to make policies robust to uncertainty:

| Randomization Type | Example Parameters |
|--------------------|-------------------|
| Physics | friction coefficients, mass, damping |
| Dynamics | actuator delay, action noise |
| Perception | camera pose, lighting, textures |
| Contacts | contact geometry, stiffness |

Key findings (Tobin et al.):
- **Non-realistic textures** (random RGB, gradients, checkerboard) are sufficient
- Performance degrades significantly when fewer than 1,000 textures are used (Figure 5)
- No real data fine-tuning required for successful transfer

### 3.3 Application to Locomotion Control (Hwangbo et al.)

Randomization strategy for the ANYmal quadruped:

```python
# Physical parameter randomization
randomization = {
    "mass": Uniform(0.5, 1.5),           # mass ±50%
    "friction": Uniform(0.7, 1.3),       # friction ±30%
    "joint_damping": LogUniform(0.3, 3), # damping 0.3-3x
    "com_position": Uniform(-2, 2) cm,   # center of mass offset
}