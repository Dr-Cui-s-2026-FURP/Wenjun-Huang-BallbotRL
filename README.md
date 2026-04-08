# RL Balance & Roll: Reinforcement-Learning Control of a Ballbot



---

## 📖 1. Project Background & Overview (Start Here)x

### 1.1 The Challenge of Dynamic Balance: From Segways to Ballbots

Have you ever tried to balance a broomstick on the palm of your hand? It requires constant, microscopic adjustments to keep the stick from falling over. This is known in physics and control theory as the **"Inverted Pendulum"** problem.

- **Two-Wheeled Balancing Robots:** Think of a Segway. It balances by driving its two wheels forward or backward depending on which way it is leaning. It is relatively easy to understand but only restricted to moving forward, backward, and turning.
- **Ballbots:** A Ballbot is a highly advanced robot that balances entirely on a single sphere (a ball). Because it sits on a ball, it is **omni-directional**—it can glide smoothly in any direction at any moment without having to turn first. However, controlling it is phenomenally difficult. It is highly unstable, multi-degree-of-freedom, and requires coordinating multiple motors driving the sphere simultaneously just to stay upright.

### 1.2 Enter Reinforcement Learning (RL)

Traditionally, engineers spend months deriving complex mathematical physics equations (like PID or LQR controllers) to keep these robots balanced. In this project, we throw away the manual math and use **Reinforcement Learning (RL)**.
RL is how humans and animals learn: **Trial and Error**. We will put a digital brain inside the robot and let it try to move. If it falls over, it receives a "punishment" (negative reward). If it stays upright and moves toward a target, it receives a "reward." Over millions of digital attempts, the AI discovers its own optimal way to balance and roll.

### 1.3 The Power of IsaacLab Simulation

To let an AI fail millions of times, we cannot use a real robot (it would break in 5 minutes!). Instead, we use **NVIDIA IsaacLab**. IsaacLab is a state-of-the-art physics simulation environment built on top of Isaac Sim. It utilizes the massive parallel processing power of GPUs. Instead of training one virtual robot, IsaacLab allows us to spawn 4,000 virtual robots on a single graphics card, training them all simultaneously. What takes years in real-time can be simulated in a few hours!

### 1.4 The Sim2Real Gap

Training an AI in a perfect virtual world is one thing, but the real world has friction, motor lag, sensory noise, and unpredictable bumps. When code that works perfectly in a simulation fails on real hardware, it is called the **"Sim2Real Gap"**. Overcoming this gap (using techniques like *Domain Randomization*) is the holy grail of modern robotics.

### 1.5 Your Mission

Your journey will advance in three stages. First, you will build basic RL locomotion tasks for a simpler **Two-Wheeled Robot** in simulation. Once you master that, you will step up to the complex, multi-degree-of-freedom **Ballbot**. Finally, utilizing the hardware provided by the **Control Systems Laboratory**, you will attempt to bridge the Sim2Real gap and deploy your trained AI brain directly onto physical robots!

---

## 🎯 2. Research Objectives

| Priority           | Objective                                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| **Primary**  | Master the IsaacLab environment and Reinforcement Learning fundamentals.                                           |
| **Primary**  | Train a robust RL locomotion policy for a pre-provided Two-Wheeled Balancing Robot in simulation.                  |
| **Primary**  | Formulate the RL environment, reward functions, and train a stable locomotion policy for a multi-DOF Ballbot.      |
| **Extended** | Successfully transfer the simulated RL policies to physical robots (Sim2Real) provided by the Control Systems Lab. |

---

## 🗺️ 3. Project Milestones (9 Nodes)

This project is divided into three progressive phases, combining introductory learning, core research replication, and novel hardware deployment.

### Phase 1: Onboarding & Foundations (The Basics 1/3)

*Objective: Understand RL theory and set up the GPU-accelerated IsaacLab environment.*

- [X] **Node 1: IsaacLab & RL Environment Setup**
    - Install NVIDIA Isaac Sim and IsaacLab on a GPU-enabled workstation.
    - Run introductory RL examples (e.g., Cartpole or Anymal) provided in IsaacLab to verify the installation.
- [X] **Node 2: Literature Review on RL Locomotion**
    - Read seminal papers on Deep Reinforcement Learning applied to balancing/legged robots (e.g., PPO algorithm, Sim2Real transfer).
    - *Deliverable:* A brief reading report outlining why RL is used over traditional control theory for these specific robots.
- [ ] **Node 3: Two-Wheeled Robot Sim Familiarization**
    - Load the provided URDF/Assets of the Two-Wheeled Robot into IsaacLab.
    - Set up the action space (motor torques/velocities) and observation space (IMU data, joint positions).
    - *Deliverable:* A screenshot/short video of the robot spawned in the IsaacLab environment.

### Phase 4: Policy Training & Ballbot Transition (The Core Work 1/3)

*Objective: Train the AI to balance the two-wheeled bot, then scale up the complexity to the Ballbot.*

- [ ] **Node 4: RL Locomotion on the Two-Wheeled Robot**
    - Design a reward function (penalize falling, reward moving towards a target velocity).
    - Train the policy using standard RL algorithms (e.g., PPO) until the robot can balance and follow velocity commands.
    - *Deliverable:* A video of the Two-Wheeled bot successfully driving around in simulation.
- [ ] **Node 5: Ballbot Environment Architecture**
    - Import the complex Ballbot CAD/URDF model into IsaacLab.
    - Formulate the new, high-dimensional observation space and action space required to control the ball via internal omniwheels.
- [ ] **Node 6: RL Locomotion on the Ballbot**
    - Tune the reward function aggressively. Train the Ballbot to reject disturbances (e.g., digital pushes) and roll to specific waypoints.
    - *Deliverable:* Training graphs (reward curves) and a simulation video showing stable Ballbot locomotion.

### Phase 3: Innovation & Sim2Real Deployment (The Research Frontier 1/3)

*Objective: Prepare the digital brain for the messy real world and deploy it to physical hardware.*

- [ ] **Node 7: Domain Randomization (Sim2Real Prep)**
    - To prepare for physical hardware, introduce "noise" into your simulation. Randomize friction, robot mass, motor delays, and sensor latency in IsaacLab.
    - Re-train your policies so the AI learns to adapt to unpredictable physics.
    - *Deliverable:* A comparative report showing policy robustness with vs. without Domain Randomization.
- [ ] **Node 8: Sim2Real on the Two-Wheeled Robot**
    - Working with the Control Systems Lab, deploy your robust RL policy onto the physical Two-Wheeled Balancing Robot.
    - *Deliverable:* A log of hardware deployment challenges and a video of the real robot balancing using your code!
- [ ] **Node 9: Sim2Real on the Physical Ballbot (The Ultimate Test)**
    - Deploy the Ballbot policy to the real physical Ballbot hardware.
    - Evaluate its performance, record telemetry data, and finalize all deliverables.
    - *Deliverable:* Final demonstration, data logs, and preparation of the Academic Poster for the FURP Showcase.

---

## 🎓 4. Evaluation & Certificate Requirements

To successfully complete this FURP project and receive the official participation certificate, students **must** strictly meet these criteria:

1. **Milestone Completion**: Successfully complete, code, and document at least **50% of the project milestones (5 out of 9 Nodes)**.
2. **Poster Submission**: Submit a formal academic poster summarizing the RL reward design, training curves, and Sim2Real results to the annual **FURP Showcase event**.
3. **Repository Standard**: All evaluations are derived from this GitHub repository. Ensure your code, URDF files, training scripts, and logs are meticulously maintained.

---

## 🗂️ 5. Repository Structure Requirements

Students must create a personal repository within the designated GitHub Organization (e.g., `FirstnameLastname-BallbotRL`). Requirements:

```text
FirstnameLastname-BallbotRL/
├── README.md                    # Project introduction 
├── docs/                        # Literature reviews, Sim2Real notes, algorithms
├── logs/                        # Weekly work logs (e.g., logs/2026-03-10.md)
├── src/                         # Core Python scripts (IsaacLab envs, PPO training configs)
├── assets/                      # Robot URDFs, meshes, and evaluation graphs
├── checkpoints/                 # Saved Neural Network weights (.pt or .pth files)
└── poster/                      # Final FURP Showcase poster (PDF + Source)
```
