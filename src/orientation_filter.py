import starfile
import numpy as np
import pandas as pd
from scipy.spatial import transform, distance

# Insert a list of .star-files describing the outcome of the same Refine3D job
file_list = ["/home/Medalia/BWimmer/SPA/240308-Amy16-Relion/Refine3D/job101/run_data.star",
             "/home/Medalia/BWimmer/SPA/240308-Amy16-Relion/Refine3D/job138/run_data.star",
             "/home/Medalia/BWimmer/SPA/240308-Amy16-Relion/Refine3D/job139/run_data.star"]

# Construct output dataframe
comp_df = pd.DataFrame()

# Iterate over files, add to comparison dataframe
for i in range(len(file_list)):

    file = starfile.read(file_list[0], always_dict=True)
    
    particles = file['particles']
     
    # From the Relion Wiki:
    # "The first rotation is called rlnAngleRot and is around the Z-axis.
    #  The second rotation is called rlnAngleTilt and is around the new Y-axis.
    #  The third rotation is called rlnAnglePsi and is around the new Z axis"
        
    euler_angles = particles[['rlnAngleRot','rlnAngleTilt','rlnAnglePsi']].values
    quaternions = transform.Rotation.from_euler("ZYZ", euler_angles, degrees=True).as_quat()
    comp_df[f'quaternions_{i}'] = np.split(quaternions, len(particles.index))
    
    shifts = particles[['rlnOriginXAngst','rlnOriginYAngst']].values
    
    comp_df[f'shifts_{i}'] = np.split(shifts, len(particles.index))
    
# Once all information has been added, calculate distances between each set of quaternions, and each set of shifts

# Plot distribution of distances

# Filter

# Calculate mean

# Transform back to Euler

# New star file
