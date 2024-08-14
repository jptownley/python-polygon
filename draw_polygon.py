import matplotlib.pyplot as plt
import numpy as np

# Parameters
radius = 5  # Radius of the hexagon
center = (0, 0)  # Center of the hexagon

# Calculate the vertices of the hexagon
# We need 7 points to close the hexagon (6 corners + 1 repeated start point)
angles = np.linspace(0, 2 * np.pi, 7)  # Generate 7 equally spaced angles from 0 to 2*pi (360 degrees)
vertices = np.array([
    (center[0] + radius * np.cos(angle), center[1] + radius * np.sin(angle))  # Calculate x and y for each angle
    for angle in angles
])

# Create a new figure
fig, ax = plt.subplots()

# Create a polygon patch
# The 'closed=True' parameter ensures that the shape is closed
polygon = plt.Polygon(vertices, closed=True, color='blue')

# Add the polygon to the plot
ax.add_patch(polygon)

# Set limits and aspect ratio
# This ensures the hexagon is centered and fully visible
ax.set_xlim(-radius - 1, radius + 1)
ax.set_ylim(-radius - 1, radius + 1)
ax.set_aspect('equal')

# Remove axes for clarity
ax.axis('off')

# Save the figure to a file
plt.savefig('blue_hexagon.png', bbox_inches='tight', pad_inches=0.1)

# Display the plot (optional)
plt.show()