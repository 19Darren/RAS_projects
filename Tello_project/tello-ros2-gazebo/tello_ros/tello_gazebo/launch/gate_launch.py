<sdf version='1.7'>
  <world name='default'>
    <physics name='normal' type='ode'>
      <real_time_update_rate>1000</real_time_update_rate>
      <max_step_size>0.001</max_step_size>
      <real_time_factor>1</real_time_factor>
    </physics>
    <model name='ground_plane'>
      <static>1</static>
      <link name='link'>
        <collision name='collision'>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>100</mu>
                <mu2>50</mu2>
              </ode>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <contact>
              <ode/>
            </contact>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='visual'>
          <cast_shadows>0</cast_shadows>
          <geometry>
            <plane>
              <normal>0 0 1</normal>
              <size>100 100</size>
            </plane>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
          </material>
        </visual>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
    </model>
    <light name='sun' type='directional'>
      <cast_shadows>1</cast_shadows>
      <pose>0 0 10 0 -0 0</pose>
      <diffuse>0.8 0.8 0.8 1</diffuse>
      <specular>0.2 0.2 0.2 1</specular>
      <attenuation>
        <range>1000</range>
        <constant>0.9</constant>
        <linear>0.01</linear>
        <quadratic>0.001</quadratic>
      </attenuation>
      <direction>-0.5 0.1 -0.9</direction>
      <spot>
        <inner_angle>0</inner_angle>
        <outer_angle>0</outer_angle>
        <falloff>0</falloff>
      </spot>
    </light>
    <gravity>0 0 -9.8</gravity>
    <magnetic_field>6e-06 2.3e-05 -4.2e-05</magnetic_field>
    <atmosphere type='adiabatic'/>
    <scene>
      <ambient>0.4 0.4 0.4 1</ambient>
      <background>0.7 0.7 0.7 1</background>
      <shadows>1</shadows>
    </scene>
    <wind/>
    <spherical_coordinates>
      <surface_model>EARTH_WGS84</surface_model>
      <latitude_deg>0</latitude_deg>
      <longitude_deg>0</longitude_deg>
      <elevation>0</elevation>
      <heading_deg>0</heading_deg>
    </spherical_coordinates>
    <model name='tello_1'>
      <link name='base_link_1'>
        <inertial>
          <pose>3e-06 0 0 0 -0 0</pose>
          <mass>0.10001</mass>
          <inertia>
            <ixx>0.000291833</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.000541012</iyy>
            <iyz>0</iyz>
            <izz>0.000291845</izz>
          </inertia>
        </inertial>
        <collision name='base_link_1_fixed_joint_lump__collision_collision'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.18 0.18 0.05</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <contact>
              <ode/>
            </contact>
            <bounce/>
            <friction>
              <torsional>
                <ode/>
              </torsional>
              <ode/>
            </friction>
          </surface>
        </collision>
        <collision name='base_link_1_fixed_joint_lump__camera_link_1_collision_1'>
          <pose>0.035 0 0 0 -0 0</pose>
          <geometry>
            <sphere>
              <radius>0.01</radius>
            </sphere>
          </geometry>
          <surface>
            <contact>
              <ode/>
            </contact>
            <friction>
              <ode/>
              <torsional>
                <ode/>
              </torsional>
            </friction>
            <bounce/>
          </surface>
          <max_contacts>10</max_contacts>
        </collision>
        <visual name='base_link_1_visual'>
          <pose>0 0 0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.07 0.02 0.02</size>
            </box>
          </geometry>
        </visual>
        <visual name='base_link_1_visual_1'>
          <pose>0 0 -0.01 0 -0 0</pose>
          <geometry>
            <box>
              <size>0.07 0.02 0.02</size>
            </box>
          </geometry>
        </visual>
        <visual name='base_link_1_visual_2'>
          <pose>0.05 -0.05 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <length>0.01</length>
              <radius>0.045</radius>
            </cylinder>
          </geometry>
        </visual>
        <visual name='base_link_1_visual_3'>
          <pose>-0.05 0.05 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <length>0.01</length>
              <radius>0.045</radius>
            </cylinder>
          </geometry>
        </visual>
        <visual name='base_link_1_visual_4'>
          <pose>-0.05 -0.05 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <length>0.01</length>
              <radius>0.045</radius>
            </cylinder>
          </geometry>
        </visual>
        <visual name='base_link_1_visual_5'>
          <pose>0.05 0.05 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <length>0.01</length>
              <radius>0.045</radius>
            </cylinder>
          </geometry>
        </visual>
        <visual name='base_link_1_fixed_joint_lump__camera_link_1_visual_6'>
          <pose>0.035 0 0 0 -0 0</pose>
          <geometry>
            <sphere>
              <radius>0.01</radius>
            </sphere>
          </geometry>
        </visual>
        <sensor name='drone1' type='camera'>
          <update_rate>30</update_rate>
          <camera name='head'>
            <horizontal_fov>0.96</horizontal_fov>
            <image>
              <width>960</width>
              <height>720</height>
              <format>R8G8B8</format>
            </image>
            <clip>
              <near>0.1</near>
              <far>300</far>
            </clip>
            <noise>
              <type>gaussian</type>
              <mean>0</mean>
              <stddev>0.007</stddev>
            </noise>
          </camera>
          <plugin name='camera_controller_1' filename='libgazebo_ros_camera.so'>
            <alwaysOn>1</alwaysOn>
            <updateRate>0.0</updateRate>
            <cameraName>this_is_ignored</cameraName>
            <imageTopicName>image_raw</imageTopicName>
            <cameraInfoTopicName>camera_info</cameraInfoTopicName>
            <frameName>camera_link_1</frameName>
            <hackBaseline>0.07</hackBaseline>
            <distortionK1>0.0</distortionK1>
            <distortionK2>0.0</distortionK2>
            <distortionK3>0.0</distortionK3>
            <distortionT1>0.0</distortionT1>
            <distortionT2>0.0</distortionT2>
          </plugin>
          <pose>0.035 0 0 0 -0 0</pose>
        </sensor>
        <self_collide>0</self_collide>
        <enable_wind>0</enable_wind>
        <kinematic>0</kinematic>
      </link>
      <plugin name='TelloPlugin' filename='libTelloPlugin.so'>
        <namespace>drone1</namespace>
        <parameter name='use_sim_time' type='bool'>1</parameter>
        <link_name>base_link_1</link_name>
        <center_of_mass>0 0 0</center_of_mass>
      </plugin>
      <static>0</static>
      <plugin name='ground_truth' filename='libgazebo_ros_p3d.so'>
        <frame_name>map</frame_name>
        <body_name>base_link_1</body_name>
        <topic_name>odom</topic_name>
        <update_rate>30.0</update_rate>
      </plugin>
      <pose>0 0 1 0 -0 0</pose>
    </model>
    <model name='Gate_90'>
      <model name='Gate_1'>
        <link name='link_0'>
          <inertial>
            <mass>1</mass>
            <inertia>
              <ixx>0.145833</ixx>
              <ixy>0</ixy>
              <ixz>0</ixz>
              <iyy>0.145833</iyy>
              <iyz>0</iyz>
              <izz>0.125</izz>
            </inertia>
            <pose>0 0 0 0 -0 0</pose>
          </inertial>
          <pose>2.7998 -2.3165 0.500001 0 -0 0</pose>
          <gravity>1</gravity>
          <self_collide>0</self_collide>
          <kinematic>0</kinematic>
          <enable_wind>0</enable_wind>
          <visual name='visual'>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <material>
              <lighting>1</lighting>
              <script>
                <uri>file://media/materials/scripts/gazebo.material</uri>
                <name>Gazebo/Grey</name>
              </script>
              <shader type='pixel'>
                <normal_map>__default__</normal_map>
              </shader>
              <ambient>0.3 0.3 0.3 1</ambient>
              <diffuse>0.7 0.7 0.7 1</diffuse>
              <specular>0.01 0.01 0.01 1</specular>
              <emissive>0 0 0 1</emissive>
            </material>
            <transparency>0</transparency>
            <cast_shadows>1</cast_shadows>
          </visual>
          <collision name='collision'>
            <laser_retro>0</laser_retro>
            <max_contacts>10</max_contacts>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <surface>
              <friction>
                <ode>
                  <mu>1</mu>
                  <mu2>1</mu2>
                  <fdir1>0 0 0</fdir1>
                  <slip1>0</slip1>
                  <slip2>0</slip2>
                </ode>
                <torsional>
                  <coefficient>1</coefficient>
                  <patch_radius>0</patch_radius>
                  <surface_radius>0</surface_radius>
                  <use_patch_radius>1</use_patch_radius>
                  <ode>
                    <slip>0</slip>
                  </ode>
                </torsional>
              </friction>
              <bounce>
                <restitution_coefficient>0</restitution_coefficient>
                <threshold>1e+06</threshold>
              </bounce>
              <contact>
                <collide_without_contact>0</collide_without_contact>
                <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
                <collide_bitmask>1</collide_bitmask>
                <ode>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                  <max_vel>0.01</max_vel>
                  <min_depth>0</min_depth>
                </ode>
                <bullet>
                  <split_impulse>1</split_impulse>
                  <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                </bullet>
              </contact>
            </surface>
          </collision>
        </link>
        <link name='link_0_clone_0'>
          <inertial>
            <mass>1</mass>
            <inertia>
              <ixx>0.145833</ixx>
              <ixy>0</ixy>
              <ixz>0</ixz>
              <iyy>0.145833</iyy>
              <iyz>0</iyz>
              <izz>0.125</izz>
            </inertia>
            <pose>0 0 0 0 -0 0</pose>
          </inertial>
          <pose>2.7998 -1.82126 1.39505 0 -0 0</pose>
          <gravity>1</gravity>
          <self_collide>0</self_collide>
          <kinematic>0</kinematic>
          <enable_wind>0</enable_wind>
          <visual name='visual'>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <material>
              <lighting>1</lighting>
              <script>
                <uri>file://media/materials/scripts/gazebo.material</uri>
                <name>Gazebo/Grey</name>
              </script>
              <shader type='pixel'>
                <normal_map>__default__</normal_map>
              </shader>
              <ambient>0 1 0 0</ambient>
              <diffuse>0 1 0 0</diffuse>
              <specular>0 1 0 0</specular>
              <emissive>0 0 0 1</emissive>
            </material>
            <transparency>0</transparency>
            <cast_shadows>1</cast_shadows>
          </visual>
          <collision name='collision'>
            <laser_retro>0</laser_retro>
            <max_contacts>10</max_contacts>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <surface>
              <friction>
                <ode>
                  <mu>1</mu>
                  <mu2>1</mu2>
                  <fdir1>0 0 0</fdir1>
                  <slip1>0</slip1>
                  <slip2>0</slip2>
                </ode>
                <torsional>
                  <coefficient>1</coefficient>
                  <patch_radius>0</patch_radius>
                  <surface_radius>0</surface_radius>
                  <use_patch_radius>1</use_patch_radius>
                  <ode>
                    <slip>0</slip>
                  </ode>
                </torsional>
              </friction>
              <bounce>
                <restitution_coefficient>0</restitution_coefficient>
                <threshold>1e+06</threshold>
              </bounce>
              <contact>
                <collide_without_contact>0</collide_without_contact>
                <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
                <collide_bitmask>1</collide_bitmask>
                <ode>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                  <max_vel>0.01</max_vel>
                  <min_depth>0</min_depth>
                </ode>
                <bullet>
                  <split_impulse>1</split_impulse>
                  <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                </bullet>
              </contact>
            </surface>
          </collision>
        </link>
        <link name='link_0_clone_0_clone'>
          <inertial>
            <mass>1</mass>
            <inertia>
              <ixx>0.145833</ixx>
              <ixy>0</ixy>
              <ixz>0</ixz>
              <iyy>0.145833</iyy>
              <iyz>0</iyz>
              <izz>0.125</izz>
            </inertia>
            <pose>0 0 0 0 -0 0</pose>
          </inertial>
          <pose>2.7998 -2.27164 1.84407 1.56884 -0 0</pose>
          <gravity>1</gravity>
          <self_collide>0</self_collide>
          <kinematic>0</kinematic>
          <enable_wind>0</enable_wind>
          <visual name='visual'>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <material>
              <lighting>1</lighting>
              <script>
                <uri>file://media/materials/scripts/gazebo.material</uri>
                <name>Gazebo/Grey</name>
              </script>
              <shader type='pixel'>
                <normal_map>__default__</normal_map>
              </shader>
              <ambient>0 1 0 0</ambient>
              <diffuse>0 1 0 0</diffuse>
              <specular>0 1 0 0</specular>
              <emissive>0 0 0 1</emissive>
            </material>
            <transparency>0</transparency>
            <cast_shadows>1</cast_shadows>
          </visual>
          <collision name='collision'>
            <laser_retro>0</laser_retro>
            <max_contacts>10</max_contacts>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <surface>
              <friction>
                <ode>
                  <mu>1</mu>
                  <mu2>1</mu2>
                  <fdir1>0 0 0</fdir1>
                  <slip1>0</slip1>
                  <slip2>0</slip2>
                </ode>
                <torsional>
                  <coefficient>1</coefficient>
                  <patch_radius>0</patch_radius>
                  <surface_radius>0</surface_radius>
                  <use_patch_radius>1</use_patch_radius>
                  <ode>
                    <slip>0</slip>
                  </ode>
                </torsional>
              </friction>
              <bounce>
                <restitution_coefficient>0</restitution_coefficient>
                <threshold>1e+06</threshold>
              </bounce>
              <contact>
                <collide_without_contact>0</collide_without_contact>
                <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
                <collide_bitmask>1</collide_bitmask>
                <ode>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                  <max_vel>0.01</max_vel>
                  <min_depth>0</min_depth>
                </ode>
                <bullet>
                  <split_impulse>1</split_impulse>
                  <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                </bullet>
              </contact>
            </surface>
          </collision>
        </link>
        <link name='link_0_clone_0_clone_0'>
          <inertial>
            <mass>1</mass>
            <inertia>
              <ixx>0.145833</ixx>
              <ixy>0</ixy>
              <ixz>0</ixz>
              <iyy>0.145833</iyy>
              <iyz>0</iyz>
              <izz>0.125</izz>
            </inertia>
            <pose>0 0 0 0 -0 0</pose>
          </inertial>
          <pose>2.7998 -2.72174 1.39505 0 -0 0</pose>
          <gravity>1</gravity>
          <self_collide>0</self_collide>
          <kinematic>0</kinematic>
          <enable_wind>0</enable_wind>
          <visual name='visual'>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <material>
              <lighting>1</lighting>
              <script>
                <uri>file://media/materials/scripts/gazebo.material</uri>
                <name>Gazebo/Grey</name>
              </script>
              <shader type='pixel'>
                <normal_map>__default__</normal_map>
              </shader>
              <ambient>0 1 0 0</ambient>
              <diffuse>0 1 0 0</diffuse>
              <specular>0 1 0 0</specular>
              <emissive>0 0 0 1</emissive>
            </material>
            <transparency>0</transparency>
            <cast_shadows>1</cast_shadows>
          </visual>
          <collision name='collision'>
            <laser_retro>0</laser_retro>
            <max_contacts>10</max_contacts>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <surface>
              <friction>
                <ode>
                  <mu>1</mu>
                  <mu2>1</mu2>
                  <fdir1>0 0 0</fdir1>
                  <slip1>0</slip1>
                  <slip2>0</slip2>
                </ode>
                <torsional>
                  <coefficient>1</coefficient>
                  <patch_radius>0</patch_radius>
                  <surface_radius>0</surface_radius>
                  <use_patch_radius>1</use_patch_radius>
                  <ode>
                    <slip>0</slip>
                  </ode>
                </torsional>
              </friction>
              <bounce>
                <restitution_coefficient>0</restitution_coefficient>
                <threshold>1e+06</threshold>
              </bounce>
              <contact>
                <collide_without_contact>0</collide_without_contact>
                <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
                <collide_bitmask>1</collide_bitmask>
                <ode>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                  <max_vel>0.01</max_vel>
                  <min_depth>0</min_depth>
                </ode>
                <bullet>
                  <split_impulse>1</split_impulse>
                  <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                </bullet>
              </contact>
            </surface>
          </collision>
        </link>
        <link name='link_0_clone_0_clone_1'>
          <inertial>
            <mass>1</mass>
            <inertia>
              <ixx>0.145833</ixx>
              <ixy>0</ixy>
              <ixz>0</ixz>
              <iyy>0.145833</iyy>
              <iyz>0</iyz>
              <izz>0.125</izz>
            </inertia>
            <pose>0 0 0 0 -0 0</pose>
          </inertial>
          <pose>2.7998 -2.2715 0.947525 1.57575 -0 0</pose>
          <gravity>1</gravity>
          <self_collide>0</self_collide>
          <kinematic>0</kinematic>
          <enable_wind>0</enable_wind>
          <visual name='visual'>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <material>
              <lighting>1</lighting>
              <script>
                <uri>file://media/materials/scripts/gazebo.material</uri>
                <name>Gazebo/Grey</name>
              </script>
              <shader type='pixel'>
                <normal_map>__default__</normal_map>
              </shader>
              <ambient>0 1 0 0</ambient>
              <diffuse>0 1 0 0</diffuse>
              <specular>0 1 0 0</specular>
              <emissive>0 0 0 1</emissive>
            </material>
            <transparency>0</transparency>
            <cast_shadows>1</cast_shadows>
          </visual>
          <collision name='collision'>
            <laser_retro>0</laser_retro>
            <max_contacts>10</max_contacts>
            <pose>0 0 0 0 -0 0</pose>
            <geometry>
              <cylinder>
                <radius>0.05</radius>
                <length>1</length>
              </cylinder>
            </geometry>
            <surface>
              <friction>
                <ode>
                  <mu>1</mu>
                  <mu2>1</mu2>
                  <fdir1>0 0 0</fdir1>
                  <slip1>0</slip1>
                  <slip2>0</slip2>
                </ode>
                <torsional>
                  <coefficient>1</coefficient>
                  <patch_radius>0</patch_radius>
                  <surface_radius>0</surface_radius>
                  <use_patch_radius>1</use_patch_radius>
                  <ode>
                    <slip>0</slip>
                  </ode>
                </torsional>
              </friction>
              <bounce>
                <restitution_coefficient>0</restitution_coefficient>
                <threshold>1e+06</threshold>
              </bounce>
              <contact>
                <collide_without_contact>0</collide_without_contact>
                <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
                <collide_bitmask>1</collide_bitmask>
                <ode>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                  <max_vel>0.01</max_vel>
                  <min_depth>0</min_depth>
                </ode>
                <bullet>
                  <split_impulse>1</split_impulse>
                  <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                  <soft_cfm>0</soft_cfm>
                  <soft_erp>0.2</soft_erp>
                  <kp>1e+13</kp>
                  <kd>1</kd>
                </bullet>
              </contact>
            </surface>
          </collision>
        </link>
        <joint name='link_0_JOINT_0' type='fixed'>
          <parent>link_0</parent>
          <child>link_0_clone_0_clone_1</child>
          <pose>0 0 0 0 -0 0</pose>
          <physics>
            <ode>
              <limit>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </limit>
              <suspension>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </suspension>
            </ode>
          </physics>
        </joint>
        <joint name='link_0_clone_0_clone_0_JOINT_4' type='fixed'>
          <parent>link_0_clone_0_clone_0</parent>
          <child>link_0_clone_0_clone</child>
          <pose>0 0 0 0 -0 0</pose>
          <physics>
            <ode>
              <limit>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </limit>
              <suspension>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </suspension>
            </ode>
          </physics>
        </joint>
        <joint name='link_0_clone_0_clone_1_JOINT_2' type='fixed'>
          <parent>link_0_clone_0_clone_1</parent>
          <child>link_0_clone_0_clone_0</child>
          <pose>0 0 0 0 -0 0</pose>
          <physics>
            <ode>
              <limit>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </limit>
              <suspension>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </suspension>
            </ode>
          </physics>
        </joint>
        <joint name='link_0_clone_0_clone_1_JOINT_5' type='fixed'>
          <parent>link_0_clone_0_clone_1</parent>
          <child>link_0_clone_0</child>
          <pose>0 0 0 0 -0 0</pose>
          <physics>
            <ode>
              <limit>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </limit>
              <suspension>
                <cfm>0</cfm>
                <erp>0.2</erp>
              </suspension>
            </ode>
          </physics>
        </joint>
        <static>0</static>
        <allow_auto_disable>1</allow_auto_disable>
        <pose>-5e-06 -4e-06 0 0 -0 0</pose>
      </model>
      <static>0</static>
      <allow_auto_disable>1</allow_auto_disable>
      <pose>0.191496 2.3318 0 0 -0 0</pose>
    </model>
    <model name='Gate_60'>
      <link name='link_0'>
        <inertial>
          <mass>0.0102102</mass>
          <inertia>
            <ixx>0.00085723</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.00085723</iyy>
            <iyz>0</iyz>
            <izz>1.276e-05</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <pose>2.20972 -2.41228 1.39604 0 0.567371 0</pose>
        <gravity>1</gravity>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <enable_wind>0</enable_wind>
        <visual name='visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <material>
            <lighting>1</lighting>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <shader type='pixel'>
              <normal_map>__default__</normal_map>
            </shader>
            <ambient>0 1 0 0</ambient>
            <diffuse>0 1 0 0</diffuse>
            <specular>0 1 0 0</specular>
            <emissive>0 1 0 0</emissive>
          </material>
          <transparency>0</transparency>
          <cast_shadows>1</cast_shadows>
        </visual>
        <collision name='collision'>
          <laser_retro>0</laser_retro>
          <max_contacts>10</max_contacts>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
                <fdir1>0 0 0</fdir1>
                <slip1>0</slip1>
                <slip2>0</slip2>
              </ode>
              <torsional>
                <coefficient>1</coefficient>
                <patch_radius>0</patch_radius>
                <surface_radius>0</surface_radius>
                <use_patch_radius>1</use_patch_radius>
                <ode>
                  <slip>0</slip>
                </ode>
              </torsional>
            </friction>
            <bounce>
              <restitution_coefficient>0</restitution_coefficient>
              <threshold>1e+06</threshold>
            </bounce>
            <contact>
              <collide_without_contact>0</collide_without_contact>
              <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
              <collide_bitmask>1</collide_bitmask>
              <ode>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
                <max_vel>0.01</max_vel>
                <min_depth>0</min_depth>
              </ode>
              <bullet>
                <split_impulse>1</split_impulse>
                <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
              </bullet>
            </contact>
          </surface>
        </collision>
      </link>
      <link name='link_0_clone'>
        <inertial>
          <mass>0.0102102</mass>
          <inertia>
            <ixx>0.00085723</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.00085723</iyy>
            <iyz>0</iyz>
            <izz>1.276e-05</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <pose>2.18918 -1.5122 1.35864 0 0.584194 0</pose>
        <gravity>1</gravity>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <enable_wind>0</enable_wind>
        <visual name='visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <material>
            <lighting>1</lighting>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <shader type='pixel'>
              <normal_map>__default__</normal_map>
            </shader>
            <ambient>0 1 0 0</ambient>
            <diffuse>0 1 0 0</diffuse>
            <specular>0 1 0 0</specular>
            <emissive>0 1 0 0</emissive>
          </material>
          <transparency>0</transparency>
          <cast_shadows>1</cast_shadows>
        </visual>
        <collision name='collision'>
          <laser_retro>0</laser_retro>
          <max_contacts>10</max_contacts>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
                <fdir1>0 0 0</fdir1>
                <slip1>0</slip1>
                <slip2>0</slip2>
              </ode>
              <torsional>
                <coefficient>1</coefficient>
                <patch_radius>0</patch_radius>
                <surface_radius>0</surface_radius>
                <use_patch_radius>1</use_patch_radius>
                <ode>
                  <slip>0</slip>
                </ode>
              </torsional>
            </friction>
            <bounce>
              <restitution_coefficient>0</restitution_coefficient>
              <threshold>1e+06</threshold>
            </bounce>
            <contact>
              <collide_without_contact>0</collide_without_contact>
              <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
              <collide_bitmask>1</collide_bitmask>
              <ode>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
                <max_vel>0.01</max_vel>
                <min_depth>0</min_depth>
              </ode>
              <bullet>
                <split_impulse>1</split_impulse>
                <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
              </bullet>
            </contact>
          </surface>
        </collision>
      </link>
      <link name='link_0_clone_0'>
        <inertial>
          <mass>0.00235619</mass>
          <inertia>
            <ixx>0.00019782</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.00019782</iyy>
            <iyz>0</iyz>
            <izz>2.95e-06</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <pose>2.5465 -1.96195 1.7911 1.56387 -0 0</pose>
        <gravity>1</gravity>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <enable_wind>0</enable_wind>
        <visual name='visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <material>
            <lighting>1</lighting>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <shader type='pixel'>
              <normal_map>__default__</normal_map>
            </shader>
            <ambient>0 1 0 0</ambient>
            <diffuse>0 1 0 0</diffuse>
            <specular>0 1 0 0</specular>
            <emissive>0 1 0 0</emissive>
          </material>
          <transparency>0</transparency>
          <cast_shadows>1</cast_shadows>
        </visual>
        <collision name='collision'>
          <laser_retro>0</laser_retro>
          <max_contacts>10</max_contacts>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
                <fdir1>0 0 0</fdir1>
                <slip1>0</slip1>
                <slip2>0</slip2>
              </ode>
              <torsional>
                <coefficient>1</coefficient>
                <patch_radius>0</patch_radius>
                <surface_radius>0</surface_radius>
                <use_patch_radius>1</use_patch_radius>
                <ode>
                  <slip>0</slip>
                </ode>
              </torsional>
            </friction>
            <bounce>
              <restitution_coefficient>0</restitution_coefficient>
              <threshold>1e+06</threshold>
            </bounce>
            <contact>
              <collide_without_contact>0</collide_without_contact>
              <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
              <collide_bitmask>1</collide_bitmask>
              <ode>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
                <max_vel>0.01</max_vel>
                <min_depth>0</min_depth>
              </ode>
              <bullet>
                <split_impulse>1</split_impulse>
                <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
              </bullet>
            </contact>
          </surface>
        </collision>
      </link>
      <link name='link_0_clone_1'>
        <inertial>
          <mass>1</mass>
          <inertia>
            <ixx>0.145833</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.145833</iyy>
            <iyz>0</iyz>
            <izz>0.125</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <pose>1.94885 -1.96224 0.949569 1.57166 -0 0</pose>
        <gravity>1</gravity>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <enable_wind>0</enable_wind>
        <visual name='visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <material>
            <lighting>1</lighting>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <shader type='pixel'>
              <normal_map>__default__</normal_map>
            </shader>
            <ambient>0 1 0 0</ambient>
            <diffuse>0 1 0 0</diffuse>
            <specular>0 1 0 0</specular>
            <emissive>0 1 0 1</emissive>
          </material>
          <transparency>0</transparency>
          <cast_shadows>1</cast_shadows>
        </visual>
        <collision name='collision'>
          <laser_retro>0</laser_retro>
          <max_contacts>10</max_contacts>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
                <fdir1>0 0 0</fdir1>
                <slip1>0</slip1>
                <slip2>0</slip2>
              </ode>
              <torsional>
                <coefficient>1</coefficient>
                <patch_radius>0</patch_radius>
                <surface_radius>0</surface_radius>
                <use_patch_radius>1</use_patch_radius>
                <ode>
                  <slip>0</slip>
                </ode>
              </torsional>
            </friction>
            <bounce>
              <restitution_coefficient>0</restitution_coefficient>
              <threshold>1e+06</threshold>
            </bounce>
            <contact>
              <collide_without_contact>0</collide_without_contact>
              <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
              <collide_bitmask>1</collide_bitmask>
              <ode>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
                <max_vel>0.01</max_vel>
                <min_depth>0</min_depth>
              </ode>
              <bullet>
                <split_impulse>1</split_impulse>
                <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
              </bullet>
            </contact>
          </surface>
        </collision>
      </link>
      <link name='link_0_clone_2'>
        <inertial>
          <mass>1</mass>
          <inertia>
            <ixx>0.145833</ixx>
            <ixy>0</ixy>
            <ixz>0</ixz>
            <iyy>0.145833</iyy>
            <iyz>0</iyz>
            <izz>0.125</izz>
          </inertia>
          <pose>0 0 0 0 -0 0</pose>
        </inertial>
        <pose>1.94885 -1.96224 0.499999 0 -0 0</pose>
        <gravity>1</gravity>
        <self_collide>0</self_collide>
        <kinematic>0</kinematic>
        <enable_wind>0</enable_wind>
        <visual name='visual'>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <material>
            <lighting>1</lighting>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Grey</name>
            </script>
            <shader type='pixel'>
              <normal_map>__default__</normal_map>
            </shader>
            <ambient>0.3 0.3 0.3 1</ambient>
            <diffuse>0.7 0.7 0.7 1</diffuse>
            <specular>0.01 0.01 0.01 1</specular>
            <emissive>0 0 0 1</emissive>
          </material>
          <transparency>0</transparency>
          <cast_shadows>1</cast_shadows>
        </visual>
        <collision name='collision'>
          <laser_retro>0</laser_retro>
          <max_contacts>10</max_contacts>
          <pose>0 0 0 0 -0 0</pose>
          <geometry>
            <cylinder>
              <radius>0.05</radius>
              <length>1</length>
            </cylinder>
          </geometry>
          <surface>
            <friction>
              <ode>
                <mu>1</mu>
                <mu2>1</mu2>
                <fdir1>0 0 0</fdir1>
                <slip1>0</slip1>
                <slip2>0</slip2>
              </ode>
              <torsional>
                <coefficient>1</coefficient>
                <patch_radius>0</patch_radius>
                <surface_radius>0</surface_radius>
                <use_patch_radius>1</use_patch_radius>
                <ode>
                  <slip>0</slip>
                </ode>
              </torsional>
            </friction>
            <bounce>
              <restitution_coefficient>0</restitution_coefficient>
              <threshold>1e+06</threshold>
            </bounce>
            <contact>
              <collide_without_contact>0</collide_without_contact>
              <collide_without_contact_bitmask>1</collide_without_contact_bitmask>
              <collide_bitmask>1</collide_bitmask>
              <ode>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
                <max_vel>0.01</max_vel>
                <min_depth>0</min_depth>
              </ode>
              <bullet>
                <split_impulse>1</split_impulse>
                <split_impulse_penetration_threshold>-0.01</split_impulse_penetration_threshold>
                <soft_cfm>0</soft_cfm>
                <soft_erp>0.2</soft_erp>
                <kp>1e+13</kp>
                <kd>1</kd>
              </bullet>
            </contact>
          </surface>
        </collision>
      </link>
      <joint name='link_0_JOINT_3' type='revolute'>
        <parent>link_0</parent>
        <child>link_0_clone_0</child>
        <pose>0 0 0 0 -0 0</pose>
        <axis>
          <xyz>1 0 0</xyz>
          <limit>
            <lower>-1.79769e+308</lower>
            <upper>1.79769e+308</upper>
            <effort>-1</effort>
            <velocity>-1</velocity>
          </limit>
          <dynamics>
            <spring_reference>0</spring_reference>
            <spring_stiffness>0</spring_stiffness>
            <damping>0</damping>
            <friction>0</friction>
          </dynamics>
        </axis>
        <physics>
          <ode>
            <limit>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </limit>
            <suspension>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </suspension>
          </ode>
        </physics>
      </joint>
      <joint name='link_0_clone_1_JOINT_1' type='fixed'>
        <parent>link_0_clone_1</parent>
        <child>link_0_clone</child>
        <pose>0 0 0 0 -0 0</pose>
        <physics>
          <ode>
            <limit>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </limit>
            <suspension>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </suspension>
          </ode>
        </physics>
      </joint>
      <joint name='link_0_clone_1_JOINT_2' type='fixed'>
        <parent>link_0_clone_1</parent>
        <child>link_0</child>
        <pose>0 0 0 0 -0 0</pose>
        <physics>
          <ode>
            <limit>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </limit>
            <suspension>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </suspension>
          </ode>
        </physics>
      </joint>
      <joint name='link_0_clone_2_JOINT_0' type='fixed'>
        <parent>link_0_clone_2</parent>
        <child>link_0_clone_1</child>
        <pose>0 0 0 0 -0 0</pose>
        <physics>
          <ode>
            <limit>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </limit>
            <suspension>
              <cfm>0</cfm>
              <erp>0.2</erp>
            </suspension>
          </ode>
        </physics>
      </joint>
      <static>0</static>
      <allow_auto_disable>1</allow_auto_disable>
      <pose>4.04916 1.93871 0 0 -0 0</pose>
    </model>
    <state world_name='default'>
      <sim_time>269 361000000</sim_time>
      <real_time>367 318245494</real_time>
      <wall_time>1653541520 840672697</wall_time>
      <iterations>269361</iterations>
      <model name='Gate_60'>
        <pose>4.25639 2.13171 -4.8e-05 -2.2e-05 4e-06 -0.103749</pose>
        <scale>1 1 1</scale>
        <link name='link_0'>
          <pose>6.20442 -0.496417 1.39603 -2.6e-05 0.567375 -0.103763</pose>
          <velocity>-0.000394 -0.000573 -0.001474 0.002763 -1e-05 0.001516</velocity>
          <acceleration>0.043787 -0.98413 -2.96392 -0.456948 1.53414 -0.665455</acceleration>
          <wrench>0.000447 -0.010048 -0.030262 0 -0 0</wrench>
        </link>
        <link name='link_0_clone'>
          <pose>6.2772 0.40094 1.35863 1.1e-05 0.584199 -0.103727</pose>
          <velocity>-5.9e-05 0.000322 -0.002249 -0.00071 -0.000163 0.000187</velocity>
          <acceleration>-0.399189 0.896476 -4.51883 0.020361 0.53803 0.03661</acceleration>
          <wrench>-0.004076 0.009153 -0.046138 0 -0 0</wrench>
        </link>
        <link name='link_0_clone_0'>
          <pose>6.58602 -0.083377 1.79109 1.55912 4e-06 -0.103749</pose>
          <velocity>0.000277 -0.001415 -0.000572 -4e-05 0.000293 0.00146</velocity>
          <acceleration>0.92483 -2.20836 -1.18923 1.78304 -0.172601 2.65665</acceleration>
          <wrench>0.002179 -0.005203 -0.002802 0 -0 0</wrench>
        </link>
        <link name='link_0_clone_1'>
          <pose>5.99156 -0.021791 0.949565 1.57166 4e-06 -0.103735</pose>
          <velocity>-8.7e-05 3.1e-05 -0.004939 -4.8e-05 -5e-06 -0.000613</velocity>
          <acceleration>0.019154 -0.031136 -9.86917 -0.023887 0.134968 0.018509</acceleration>
          <wrench>0.019154 -0.031136 -9.86917 0 -0 0</wrench>
        </link>
        <link name='link_0_clone_2'>
          <pose>5.99155 -0.021792 0.499995 -2e-06 4e-06 -0.103735</pose>
          <velocity>-7.8e-05 5e-05 -0.004942 -5.8e-05 2e-06 -0.000637</velocity>
          <acceleration>-0.017704 0.037235 -9.87484 -0.045264 0.130997 -0.026982</acceleration>
          <wrench>-0.017704 0.037235 -9.87484 0 -0 0</wrench>
        </link>
      </model>
      <model name='Gate_90'>
        <pose>0.194343 2.33412 -0.000416 -7.3e-05 -9e-05 -0.001254</pose>
        <scale>1 1 1</scale>
        <model name='Gate_1'>
          <pose>0.194338 2.33411 -0.000416 -7.3e-05 -9e-05 -0.001254</pose>
          <scale>1 1 1</scale>
          <link name='link_0'>
            <pose>2.99119 0.01414 0.500004 -7.3e-05 -9e-05 -0.001254</pose>
            <velocity>0.000639 -0.000655 -0.000733 0.00137 0.001209 -0.000466</velocity>
            <acceleration>-0.121227 -0.11885 -9.8098 0.3171 -0.338565 -0.011867</acceleration>
            <wrench>-0.121227 -0.11885 -9.8098 0 -0 0</wrench>
          </link>
          <link name='link_0_clone_0'>
            <pose>2.99173 0.509444 1.39502 -7.3e-05 -9e-05 -0.001254</pose>
            <velocity>0.002082 -0.001761 -9.3e-05 0.001332 0.001236 -0.000478</velocity>
            <acceleration>-0.036712 -0.051921 -9.76426 0.205185 -0.260089 -0.047938</acceleration>
            <wrench>-0.036712 -0.051921 -9.76426 0 -0 0</wrench>
          </link>
          <link name='link_0_clone_0_clone'>
            <pose>2.99112 0.059097 1.84407 1.56877 -9e-05 -0.001254</pose>
            <velocity>0.002513 -0.002284 -0.000675 0.001279 0.001292 -0.000491</velocity>
            <acceleration>0.091343 0.078135 -9.80507 0.049116 -0.110219 -0.072296</acceleration>
            <wrench>0.091343 0.078135 -9.80507 0 -0 0</wrench>
          </link>
          <link name='link_0_clone_0_clone_0'>
            <pose>2.9906 -0.391035 1.39508 -7.2e-05 -9e-05 -0.001254</pose>
            <velocity>0.001699 -0.001714 -0.00124 0.001268 0.001303 -0.0005</velocity>
            <acceleration>0.05922 0.086218 -9.79872 0.017908 -0.063617 -0.111413</acceleration>
            <wrench>0.05922 0.086218 -9.79872 0 -0 0</wrench>
          </link>
          <link name='link_0_clone_0_clone_1'>
            <pose>2.9912 0.059172 0.947525 1.57568 -9e-05 -0.001254</pose>
            <velocity>0.001297 -0.001176 -0.000681 0.001348 0.001221 -0.000471</velocity>
            <acceleration>0.007377 0.006418 -9.82215 0.251472 -0.352761 -0.023626</acceleration>
            <wrench>0.007377 0.006418 -9.82215 0 -0 0</wrench>
          </link>
        </model>
      </model>
      <model name='ground_plane'>
        <pose>0 0 0 0 -0 0</pose>
        <scale>1 1 1</scale>
        <link name='link'>
          <pose>0 0 0 0 -0 0</pose>
          <velocity>0 0 0 0 -0 0</velocity>
          <acceleration>0 0 0 0 -0 0</acceleration>
          <wrench>0 0 0 0 -0 0</wrench>
        </link>
      </model>
      <model name='tello_1'>
        <pose>1.2e-05 0 1.2925 0 0.00135 0</pose>
        <scale>1 1 1</scale>
        <link name='base_link_1'>
          <pose>1.2e-05 0 1.2925 0 0.00135 0</pose>
          <velocity>0 0 0 0 1.35049 0</velocity>
          <acceleration>-0 -0 -0 0 0.005435 0</acceleration>
          <wrench>-0 -0 -0 0 -0 0</wrench>
        </link>
      </model>
      <light name='sun'>
        <pose>0 0 10 0 -0 0</pose>
      </light>
    </state>
    <gui fullscreen='0'>
      <camera name='user_camera'>
        <pose>9.67141 -5.54159 2.86044 0 0.275643 2.35619</pose>
        <view_controller>orbit</view_controller>
        <projection_type>perspective</projection_type>
      </camera>
    </gui>
  </world>
</sdf>
