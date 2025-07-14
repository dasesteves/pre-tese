import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Polygon
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta

# Set style
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# Figure 2.1 - Healthcare IT Evolution Timeline
def create_healthcare_it_timeline():
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Timeline data
    events = [
        {'year': 1960, 'event': 'Mainframe Systems', 'desc': 'Centralized computing', 'y': 0.2},
        {'year': 1980, 'event': 'Departmental Systems', 'desc': 'Specialized applications', 'y': 0.8},
        {'year': 1990, 'event': 'HL7 Integration', 'desc': 'Standardized messaging', 'y': 0.3},
        {'year': 2000, 'event': 'Web-based EMR', 'desc': 'Internet technologies', 'y': 0.7},
        {'year': 2010, 'event': 'Cloud & Mobile', 'desc': 'SaaS solutions', 'y': 0.4},
        {'year': 2020, 'event': 'AI & Interoperability', 'desc': 'FHIR, Machine Learning', 'y': 0.6},
        {'year': 2024, 'event': 'Integrated Platforms', 'desc': 'Unified ecosystems', 'y': 0.5}
    ]
    
    # Draw timeline
    ax.plot([1960, 2024], [0.5, 0.5], 'k-', linewidth=3)
    
    # Add events
    for event in events:
        # Event marker
        ax.scatter(event['year'], 0.5, s=200, c='blue', zorder=5)
        
        # Event box
        if event['y'] > 0.5:
            y_box = event['y']
            va = 'bottom'
            arrow_start = y_box - 0.05
        else:
            y_box = event['y']
            va = 'top'
            arrow_start = y_box + 0.05
            
        # Draw arrow
        ax.annotate('', xy=(event['year'], 0.5), xytext=(event['year'], arrow_start),
                   arrowprops=dict(arrowstyle='-', lw=1, color='gray'))
        
        # Event text box
        bbox_props = dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8)
        ax.text(event['year'], y_box, f"{event['event']}\n{event['desc']}", 
                ha='center', va=va, fontsize=10, bbox=bbox_props)
    
    # Title and labels
    ax.set_title('Evolution of Healthcare Information Systems', fontsize=16, fontweight='bold')
    ax.set_xlabel('Year', fontsize=12)
    ax.set_xlim(1955, 2030)
    ax.set_ylim(0, 1)
    ax.set_yticks([])
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('images/generated/healthcare_it_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 4.2 - JWT Authentication Flow
def create_jwt_flow():
    fig, ax = plt.subplots(figsize=(12, 10))
    
    # Define components
    components = {
        'Client': {'pos': (2, 8), 'color': '#e3f2fd'},
        'API Gateway': {'pos': (6, 8), 'color': '#f3e5f5'},
        'Auth Service': {'pos': (10, 8), 'color': '#e8f5e9'},
        'LDAP': {'pos': (10, 5), 'color': '#fff3e0'},
        'Database': {'pos': (10, 2), 'color': '#ffebee'}
    }
    
    # Draw components
    for name, info in components.items():
        rect = FancyBboxPatch(
            (info['pos'][0]-1, info['pos'][1]-0.5), 2, 1,
            boxstyle="round,pad=0.1",
            facecolor=info['color'],
            edgecolor='darkgray',
            linewidth=2
        )
        ax.add_patch(rect)
        ax.text(info['pos'][0], info['pos'][1], name, ha='center', va='center', 
                fontsize=11, fontweight='bold')
    
    # Define flow steps
    flows = [
        {'from': 'Client', 'to': 'API Gateway', 'label': '1. Login Request\n(username/password)', 'style': 'solid'},
        {'from': 'API Gateway', 'to': 'Auth Service', 'label': '2. Validate\nCredentials', 'style': 'solid'},
        {'from': 'Auth Service', 'to': 'LDAP', 'label': '3. LDAP\nAuthentication', 'style': 'solid'},
        {'from': 'LDAP', 'to': 'Auth Service', 'label': '4. User Details', 'style': 'dashed'},
        {'from': 'Auth Service', 'to': 'Database', 'label': '5. Get User\nRoles/Permissions', 'style': 'solid'},
        {'from': 'Database', 'to': 'Auth Service', 'label': '6. Return\nPermissions', 'style': 'dashed'},
        {'from': 'Auth Service', 'to': 'API Gateway', 'label': '7. Generate JWT\n(with claims)', 'style': 'dashed'},
        {'from': 'API Gateway', 'to': 'Client', 'label': '8. Return JWT\n(httpOnly cookie)', 'style': 'dashed'}
    ]
    
    # Draw flows
    for i, flow in enumerate(flows):
        from_pos = components[flow['from']]['pos']
        to_pos = components[flow['to']]['pos']
        
        # Calculate arrow position
        if from_pos[0] == to_pos[0]:  # Vertical
            if from_pos[1] > to_pos[1]:  # Down
                start = (from_pos[0], from_pos[1] - 0.5)
                end = (to_pos[0], to_pos[1] + 0.5)
            else:  # Up
                start = (from_pos[0], from_pos[1] + 0.5)
                end = (to_pos[0], to_pos[1] - 0.5)
        else:  # Horizontal
            if from_pos[0] < to_pos[0]:  # Right
                start = (from_pos[0] + 1, from_pos[1])
                end = (to_pos[0] - 1, to_pos[1])
            else:  # Left
                start = (from_pos[0] - 1, from_pos[1])
                end = (to_pos[0] + 1, to_pos[1])
        
        # Draw arrow
        arrow_style = '->' if flow['style'] == 'solid' else '<-'
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle=arrow_style, lw=2, 
                                 color='blue' if flow['style'] == 'solid' else 'green',
                                 linestyle=flow['style']))
        
        # Add label
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x, mid_y, flow['label'], ha='center', va='center', 
                fontsize=9, bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    # Title
    ax.set_title('JWT Authentication Flow with LDAP Integration', fontsize=16, fontweight='bold')
    
    # Legend
    ax.plot([], [], 'b-', linewidth=2, label='Request')
    ax.plot([], [], 'g--', linewidth=2, label='Response')
    ax.legend(loc='lower right')
    
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/generated/jwt_authentication_flow.png', dpi=300, bbox_inches='tight')
    plt.close()

# Table 2.1 - System Comparison
def create_system_comparison_table():
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis('tight')
    ax.axis('off')
    
    # Data for comparison
    headers = ['Feature', 'AIDA-PCE\n(Legacy)', 'Epic', 'Cerner', 'Our System']
    data = [
        ['Architecture', 'Monolithic', 'Integrated Suite', 'Modular', 'Microservices'],
        ['User Interface', 'Desktop Only', 'Web/Mobile', 'Web/Mobile', 'Responsive Web'],
        ['Real-time Validation', 'Limited', 'Yes', 'Yes', 'Advanced'],
        ['Integration', 'Custom APIs', 'HL7/FHIR', 'HL7/FHIR', 'RESTful/HL7'],
        ['Cloud Support', 'No', 'Hybrid', 'Yes', 'Cloud-Ready'],
        ['Cost Model', 'License', 'Subscription', 'Subscription', 'Open Source'],
        ['Customization', 'Limited', 'Moderate', 'High', 'Very High'],
        ['AI/ML Features', 'None', 'Basic', 'Advanced', 'Planned']
    ]
    
    # Create table
    table = ax.table(cellText=data, colLabels=headers, loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # Style header
    for i in range(len(headers)):
        table[(0, i)].set_facecolor('#4CAF50')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Style rows
    for i in range(1, len(data) + 1):
        for j in range(len(headers)):
            if j == 0:  # Feature column
                table[(i, j)].set_facecolor('#e3f2fd')
                table[(i, j)].set_text_props(weight='bold')
            elif j == 1:  # Legacy system
                table[(i, j)].set_facecolor('#ffebee')
            elif j == len(headers) - 1:  # Our system
                table[(i, j)].set_facecolor('#e8f5e9')
    
    plt.title('Comparison of Hospital Medication Management Systems', 
              fontsize=16, fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('images/generated/system_comparison_table.png', dpi=300, bbox_inches='tight')
    plt.close()

# Figure 4.7 - Monitoring Dashboard
def create_monitoring_dashboard():
    fig = plt.figure(figsize=(16, 10))
    
    # Create grid
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    ax1 = fig.add_subplot(gs[0, :2])  # Response time
    ax2 = fig.add_subplot(gs[0, 2])   # Uptime
    ax3 = fig.add_subplot(gs[1, :])   # Request volume
    ax4 = fig.add_subplot(gs[2, 0])   # Error types
    ax5 = fig.add_subplot(gs[2, 1])   # API usage
    ax6 = fig.add_subplot(gs[2, 2])   # Active users
    
    # 1. Response Time Trend
    hours = list(range(24))
    response_times = 150 + 50 * np.sin(np.array(hours) * np.pi / 12) + np.random.normal(0, 10, 24)
    ax1.plot(hours, response_times, 'b-', linewidth=2)
    ax1.axhline(y=200, color='r', linestyle='--', label='SLA Limit')
    ax1.fill_between(hours, response_times, alpha=0.3)
    ax1.set_title('Average Response Time (Last 24h)', fontweight='bold')
    ax1.set_xlabel('Hour')
    ax1.set_ylabel('Response Time (ms)')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # 2. Uptime Gauge
    uptime = 99.95
    colors = ['#4CAF50', '#f5f5f5']
    sizes = [uptime, 100-uptime]
    ax2.pie(sizes, colors=colors, startangle=90, counterclock=False)
    circle = Circle((0, 0), 0.7, color='white')
    ax2.add_patch(circle)
    ax2.text(0, 0, f'{uptime}%\nUptime', ha='center', va='center', 
             fontsize=16, fontweight='bold')
    ax2.set_title('System Uptime', fontweight='bold')
    
    # 3. Request Volume
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    requests = [45000, 48000, 52000, 51000, 49000, 35000, 32000]
    bars = ax3.bar(days, requests, color='#2196F3')
    ax3.set_title('Daily Request Volume (Current Week)', fontweight='bold')
    ax3.set_ylabel('Number of Requests')
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height/1000)}k', ha='center', va='bottom')
    
    # 4. Error Distribution
    error_types = ['Timeout', 'Auth', 'Validation', 'Server', 'Other']
    error_counts = [12, 8, 25, 5, 10]
    colors_err = ['#f44336', '#FF9800', '#FFEB3B', '#4CAF50', '#2196F3']
    ax4.pie(error_counts, labels=error_types, colors=colors_err, autopct='%1.1f%%')
    ax4.set_title('Error Distribution (Last 7 Days)', fontweight='bold')
    
    # 5. API Endpoint Usage
    endpoints = ['Login', 'Prescribe', 'Validate', 'Search', 'Report']
    usage = [850, 1200, 980, 650, 420]
    ax5.barh(endpoints, usage, color='#9C27B0')
    ax5.set_title('Top API Endpoints', fontweight='bold')
    ax5.set_xlabel('Calls per Hour')
    
    # 6. Active Users
    times = ['00:00', '06:00', '12:00', '18:00', '24:00']
    users = [20, 85, 150, 120, 20]
    ax6.fill_between(range(len(times)), users, alpha=0.3, color='#4CAF50')
    ax6.plot(range(len(times)), users, 'o-', color='#4CAF50', linewidth=2)
    ax6.set_title('Active Users Today', fontweight='bold')
    ax6.set_xticks(range(len(times)))
    ax6.set_xticklabels(times)
    ax6.set_ylabel('Number of Users')
    ax6.grid(True, alpha=0.3)
    
    plt.suptitle('Real-Time System Monitoring Dashboard', fontsize=18, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/monitoring_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

# Generate additional diagrams
if __name__ == "__main__":
    print("Generating additional diagrams...")
    
    create_healthcare_it_timeline()
    print("✓ Figure 2.1 - Healthcare IT Evolution Timeline")
    
    create_jwt_flow()
    print("✓ Figure 4.2 - JWT Authentication Flow")
    
    create_system_comparison_table()
    print("✓ Table 2.1 - System Comparison")
    
    create_monitoring_dashboard()
    print("✓ Figure 4.7 - Monitoring Dashboard")
    
    print("\nAll additional diagrams generated successfully!") 