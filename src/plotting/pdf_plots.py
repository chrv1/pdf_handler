import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def visualize_result(detection_result, page, scale=1.0, show_original_boundaries=False):
    """
    Visualize the interior/exterior detection results

    Parameters:
    - detection_result: Result from detect_interior_exterior
    - page: Dictionary with 'width' and 'height' properties
    - scale: Same scaling factor used in detection
    - show_original_boundaries: If True, show original boundaries instead of closed ones

    Returns:
    - matplotlib figure
    """
    width = int(page['width'] * scale)
    height = int(page['height'] * scale)
    grid = detection_result['grid']

    # For visualization, we might want to show the original boundaries
    if show_original_boundaries:
        # Create a copy of grid and replace boundary markings with original boundaries
        temp_grid = grid.copy()
        temp_grid[temp_grid == 1] = 0  # Clear current boundaries
        temp_grid[detection_result['boundaries'] == 1] = 1  # Use original boundaries
        grid = temp_grid

    # Create a colormap for visualization (0=exterior, 1=boundary, 2=interior)
    colors = np.zeros((height, width, 3))

    for y in range(height):
        for x in range(width):
            if grid[y, x] == 1:  # Boundary
                colors[y, x] = [0, 0, 0]  # Black
            elif grid[y, x] == 0:  # Exterior (water)
                colors[y, x] = [0.8, 0.8, 0.8]  # Light gray
            else:  # Interior
                colors[y, x] = [0.2, 0.6, 1.0]  # Blue

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(colors, origin='upper')
    ax.set_title('Interior vs Exterior Detection')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Add a legend
    legend_elements = [
        Rectangle((0, 0), 1, 1, color='black', label='Boundary'),
        Rectangle((0, 0), 1, 1, color=[0.8, 0.8, 0.8], label='Exterior'),
        Rectangle((0, 0), 1, 1, color=[0.2, 0.6, 1.0], label='Interior')
    ]
    ax.legend(handles=legend_elements, loc='upper right')

    return fig