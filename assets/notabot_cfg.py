import isaaclab.sim as sim_utils
from isaaclab.actuators import ImplicitActuatorCfg, DCMotorCfg
from isaaclab.assets.articulation import ArticulationCfg
from isaaclab.sensors import RayCasterCfg
from isaaclab.utils.assets import ISAACLAB_NUCLEUS_DIR
from pathlib import Path
_PROJECT_PATH = Path(__file__).resolve().parents[1] 

NotaBot_CONFIG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=f"{_PROJECT_PATH}/assets/notabot.usd",
        activate_contact_sensors=True,
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0,
            max_angular_velocity=1000.0,
            max_depenetration_velocity=100.0,
            enable_gyroscopic_forces=True,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=False,
            solver_position_iteration_count=4,
            solver_velocity_iteration_count=0,
            sleep_threshold=0.005,
            stabilization_threshold=0.001,
        ),
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.5),
        # rot=(0.7071, 0.7071, 0, 0),
        joint_pos={".*": 0.0},
        joint_vel={".*": 0.0}
    ),
    actuators={
        "wheel_actuator": ImplicitActuatorCfg(
            joint_names_expr=['wheel_right', 'wheel_left'],
            effort_limit_sim=3.8,
            velocity_limit_sim=150.0,
            stiffness=0.0,
            damping=1000000.0
        ),
    },
)

