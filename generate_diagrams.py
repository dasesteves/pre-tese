import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import numpy as np
import seaborn as sns

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Create images directory if it doesn't exist
import os
if not os.path.exists('images/generated'):
    os.makedirs('images/generated')

# Figure 1.1 - Medication Flow Process
def create_medication_flow():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define positions
    positions = {
        'prescribing': (2, 7),
        'transcribing': (6, 7),
        'dispensing': (10, 7),
        'administering': (10, 3),
        'monitoring': (6, 3)
    }
    
    # Define colors
    colors = {
        'prescribing': '#e3f2fd',
        'transcribing': '#fff3e0',
        'dispensing': '#f3e5f5',
        'administering': '#e8f5e9',
        'monitoring': '#fce4ec'
    }
    
    # Draw boxes
    for step, pos in positions.items():
        box = FancyBboxPatch(
            (pos[0]-1.5, pos[1]-0.5), 3, 1,
            boxstyle="round,pad=0.1",
            facecolor=colors[step],
            edgecolor='darkgray',
            linewidth=2
        )
        ax.add_patch(box)
        ax.text(pos[0], pos[1], step.capitalize(), 
                ha='center', va='center', fontsize=12, fontweight='bold')
    
    # Add arrows
    arrow_props = dict(arrowstyle='->', lw=2, color='darkblue')
    
    # Prescribing to Transcribing
    ax.annotate('', xy=(4.5, 7), xytext=(3.5, 7), arrowprops=arrow_props)
    
    # Transcribing to Dispensing
    ax.annotate('', xy=(8.5, 7), xytext=(7.5, 7), arrowprops=arrow_props)
    
    # Dispensing to Administering
    ax.annotate('', xy=(10, 6.5), xytext=(10, 3.5), arrowprops=arrow_props)
    
    # Administering to Monitoring
    ax.annotate('', xy=(8.5, 3), xytext=(8.5, 3), arrowprops=arrow_props)
    
    # Monitoring to Prescribing (feedback)
    ax.annotate('', xy=(3.5, 6.5), xytext=(6, 3.5), 
                arrowprops=dict(arrowstyle='->', lw=2, color='red', linestyle='dashed'))
    
    # Add error points
    error_points = [(3, 6), (7, 6), (9, 5), (9, 2), (5, 2)]
    for i, point in enumerate(error_points):
        circle = Circle(point, 0.2, color='red', alpha=0.6)
        ax.add_patch(circle)
        ax.text(point[0], point[1]-0.5, f'Error\nPoint {i+1}', 
                ha='center', va='top', fontsize=8, color='red')
    
    # Add title and labels
    ax.text(6, 8.5, 'Hospital Medication Management Process', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(4.5, 5, 'Feedback Loop', ha='center', va='center', 
            fontsize=10, color='red', style='italic')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 9)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/generated/medication_flow_process.png', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 2.2 - Swiss Cheese Model
def create_swiss_cheese_model():
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define layers
    layers = [
        'Organizational\nFactors',
        'Supervision\n& Management',
        'Preconditions\nfor Unsafe Acts',
        'Unsafe\nActs',
        'Failed\nDefenses'
    ]
    
    # Draw cheese slices
    for i, layer in enumerate(layers):
        x = i * 2 + 1
        
        # Draw slice
        rect = Rectangle((x-0.4, 1), 0.8, 6, 
                        facecolor='#ffeb3b', edgecolor='#f57c00', linewidth=2)
        ax.add_patch(rect)
        
        # Add holes (vulnerabilities)
        np.random.seed(42 + i)
        for j in range(3):
            y = np.random.uniform(2, 6)
            circle = Circle((x, y), 0.3, facecolor='white', edgecolor='#f57c00')
            ax.add_patch(circle)
        
        # Add label
        ax.text(x, 0.5, layer, ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Draw hazard path
    hazard_x = np.linspace(0, 10, 100)
    hazard_y = 4 + 0.5 * np.sin(hazard_x)
    ax.plot(hazard_x, hazard_y, 'r-', linewidth=3, label='Hazard Trajectory')
    
    # Add arrow at the end
    ax.annotate('', xy=(10.5, hazard_y[-1]), xytext=(10, hazard_y[-1]), 
                arrowprops=dict(arrowstyle='->', lw=3, color='red'))
    
    # Add labels
    ax.text(5, 7.5, 'Swiss Cheese Model of System Accidents', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    ax.text(-0.5, 4, 'Hazard', ha='center', va='center', fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.5))
    ax.text(11, hazard_y[-1], 'Accident', ha='left', va='center', fontsize=12,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='red', alpha=0.5))
    
    ax.set_xlim(-1, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/generated/swiss_cheese_model.png', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 4.1 - System Architecture
def create_system_architecture():
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Define layers and components
    layers = {
        'Presentation': {'y': 8, 'color': '#e3f2fd', 'components': ['React/Next.js', 'Material-UI', 'TypeScript']},
        'API Gateway': {'y': 6.5, 'color': '#f3e5f5', 'components': ['REST API', 'Authentication', 'Rate Limiting']},
        'Business Logic': {'y': 5, 'color': '#e8f5e9', 'components': ['Services', 'Validation', 'Business Rules']},
        'Data Access': {'y': 3.5, 'color': '#fff3e0', 'components': ['Node.js', 'Express', 'Connection Pool']},
        'Database': {'y': 2, 'color': '#ffebee', 'components': ['Oracle 11g', 'Stored Procedures', 'Indexes']}
    }
    
    # Draw layers
    for layer_name, layer_info in layers.items():
        # Main layer box
        rect = FancyBboxPatch(
            (1, layer_info['y']-0.4), 12, 0.8,
            boxstyle="round,pad=0.05",
            facecolor=layer_info['color'],
            edgecolor='darkgray',
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Layer name
        ax.text(0.5, layer_info['y'], layer_name, ha='right', va='center', 
                fontsize=12, fontweight='bold')
        
        # Components
        comp_width = 12 / len(layer_info['components'])
        for i, comp in enumerate(layer_info['components']):
            x = 1 + i * comp_width + comp_width/2
            ax.text(x, layer_info['y'], comp, ha='center', va='center', fontsize=10)
    
    # Add connections
    for i in range(len(layers) - 1):
        y1 = list(layers.values())[i]['y'] - 0.4
        y2 = list(layers.values())[i+1]['y'] + 0.4
        for x in [3, 7, 11]:
            ax.annotate('', xy=(x, y2), xytext=(x, y1),
                       arrowprops=dict(arrowstyle='<->', lw=1.5, color='blue'))
    
    # Add external systems
    external_systems = [
        {'name': 'SONHO', 'pos': (15, 6)},
        {'name': 'AIDA-PCE', 'pos': (15, 4)},
        {'name': 'Pharmacy', 'pos': (15, 2)}
    ]
    
    for system in external_systems:
        rect = FancyBboxPatch(
            (system['pos'][0]-0.8, system['pos'][1]-0.3), 1.6, 0.6,
            boxstyle="round,pad=0.05",
            facecolor='#f5f5f5',
            edgecolor='red',
            linewidth=2,
            linestyle='dashed'
        )
        ax.add_patch(rect)
        ax.text(system['pos'][0], system['pos'][1], system['name'], 
                ha='center', va='center', fontsize=10)
        
        # Connection to main system
        ax.annotate('', xy=(13, system['pos'][1]), xytext=(system['pos'][0]-0.8, system['pos'][1]),
                   arrowprops=dict(arrowstyle='<->', lw=1.5, color='red', linestyle='dashed'))
    
    # Title
    ax.text(7, 9.5, 'Medication Management System Architecture', 
            ha='center', va='center', fontsize=16, fontweight='bold')
    
    # Legend
    ax.text(1, 0.5, 'Internal Components', ha='left', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue'))
    ax.text(5, 0.5, 'External Systems', ha='left', va='center', fontsize=10,
            bbox=dict(boxstyle="round,pad=0.3", facecolor='#f5f5f5', edgecolor='red'))
    
    ax.set_xlim(-1, 17)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/generated/system_architecture.png', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 5.1 - Development Metrics
def create_development_metrics():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Code Evolution
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    loc = [5000, 8000, 12000, 18000, 25000, 32000, 38000, 42000, 45000, 48000, 50000, 52000]
    
    ax1.plot(months, loc, 'b-', linewidth=2, marker='o')
    ax1.fill_between(range(len(months)), loc, alpha=0.3)
    ax1.set_title('Lines of Code Evolution (2025)', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Lines of Code')
    ax1.grid(True, alpha=0.3)
    
    # 2. Component Distribution
    components = ['React\nComponents', 'API\nEndpoints', 'Database\nTables', 'Stored\nProcedures']
    values = [120, 45, 87, 150]
    colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']
    
    bars = ax2.bar(components, values, color=colors)
    ax2.set_title('System Components', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Count')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}', ha='center', va='bottom')
    
    # 3. Test Coverage
    test_types = ['Unit Tests', 'Integration', 'E2E', 'Total']
    coverage = [85, 92, 100, 89]
    
    bars = ax3.barh(test_types, coverage, color=['#4CAF50' if x >= 80 else '#FF9800' for x in coverage])
    ax3.set_title('Test Coverage (%)', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Coverage %')
    ax3.set_xlim(0, 100)
    
    # Add percentage labels
    for i, (bar, cov) in enumerate(zip(bars, coverage)):
        ax3.text(cov + 1, bar.get_y() + bar.get_height()/2, 
                f'{cov}%', va='center')
    
    # 4. Performance Comparison
    operations = ['Login', 'List\nPrescriptions', 'New\nPrescription', 'Validation']
    old_times = [3200, 5100, 2800, 4500]
    new_times = [120, 180, 95, 150]
    
    x = np.arange(len(operations))
    width = 0.35
    
    bars1 = ax4.bar(x - width/2, old_times, width, label='Old System', color='#f44336')
    bars2 = ax4.bar(x + width/2, new_times, width, label='New System', color='#4CAF50')
    
    ax4.set_title('Response Time Comparison (ms)', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Time (ms)')
    ax4.set_xticks(x)
    ax4.set_xticklabels(operations)
    ax4.legend()
    ax4.set_yscale('log')
    
    plt.suptitle('Medication Management System - Development Metrics', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/development_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 5.3 - Error Reduction Dashboard
def create_error_reduction_dashboard():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Error types reduction
    error_types = ['Prescription\nErrors', 'Transcription\nErrors', 'Administration\nErrors', 'Adverse\nEvents']
    before = [100, 100, 100, 100]  # Normalized to 100%
    after = [27, 11, 39, 22]  # Remaining after implementation
    
    x = np.arange(len(error_types))
    width = 0.35
    
    bars1 = ax1.bar(x - width/2, before, width, label='Before', color='#f44336', alpha=0.7)
    bars2 = ax1.bar(x + width/2, after, width, label='After', color='#4CAF50', alpha=0.7)
    
    # Add reduction percentages
    for i, (b, a) in enumerate(zip(before, after)):
        reduction = 100 - a
        ax1.text(i, 110, f'-{reduction}%', ha='center', va='bottom', 
                fontweight='bold', color='green', fontsize=12)
    
    ax1.set_ylabel('Relative Frequency (%)')
    ax1.set_title('Medication Error Reduction by Type', fontsize=14, fontweight='bold')
    ax1.set_xticks(x)
    ax1.set_xticklabels(error_types)
    ax1.legend()
    ax1.set_ylim(0, 120)
    
    # Timeline of error rates
    months = ['Baseline', 'Month 1', 'Month 2', 'Month 3', 'Month 4', 'Month 5', 'Month 6']
    error_rate = [8.5, 7.2, 5.8, 4.1, 3.2, 2.5, 2.3]
    
    ax2.plot(months, error_rate, 'ro-', linewidth=2, markersize=8)
    ax2.fill_between(range(len(months)), error_rate, alpha=0.3, color='red')
    ax2.axhline(y=2.3, color='green', linestyle='--', alpha=0.7)
    ax2.text(5.5, 2.5, 'Target: 2.3%', ha='right', va='bottom', color='green')
    
    ax2.set_ylabel('Error Rate (%)')
    ax2.set_xlabel('Time Period')
    ax2.set_title('Medication Error Rate Over Time', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 10)
    
    plt.suptitle('Medication Error Reduction Analysis', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/error_reduction_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate all diagrams
if __name__ == "__main__":
    print("Generating diagrams...")
    
    create_medication_flow()
    print("✓ Figure 1.1 - Medication Flow Process")
    
    create_swiss_cheese_model()
    print("✓ Figure 2.2 - Swiss Cheese Model")
    
    create_system_architecture()
    print("✓ Figure 4.1 - System Architecture")
    
    create_development_metrics()
    print("✓ Figure 5.1 - Development Metrics")
    
    create_error_reduction_dashboard()
    print("✓ Figure 5.3 - Error Reduction Dashboard")
    
    print("\nAll diagrams generated successfully!") 