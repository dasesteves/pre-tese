#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar figuras específicas do capítulo Resultados
Substitui listas excessivas por diagramas visuais mais eficazes
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle
import numpy as np
import seaborn as sns

# Set style for academic presentation
plt.style.use('default')
sns.set_palette("husl")

def create_system_architecture():
    """Figure 5.1 - System Architecture (5 layers)"""
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Define layers
    layers = [
        {'name': 'Presentation Layer', 'desc': 'React/Next.js Interface', 'color': '#e3f2fd', 'y': 7},
        {'name': 'Application Layer', 'desc': 'Node.js Express Server', 'color': '#f3e5f5', 'y': 5.5},
        {'name': 'Business Layer', 'desc': 'Business Logic & Validations', 'color': '#e8f5e9', 'y': 4},
        {'name': 'Data Layer', 'desc': 'Oracle 11g Database', 'color': '#fff3e0', 'y': 2.5},
        {'name': 'Integration Layer', 'desc': 'External Systems APIs', 'color': '#ffebee', 'y': 1}
    ]
    
    # Draw layers
    for layer in layers:
        rect = FancyBboxPatch(
            (1, layer['y']-0.4), 10, 0.8,
            boxstyle="round,pad=0.1",
            facecolor=layer['color'],
            edgecolor='darkgray',
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Layer name
        ax.text(6, layer['y'], layer['name'], ha='center', va='center', 
                fontsize=14, fontweight='bold')
        ax.text(6, layer['y']-0.2, layer['desc'], ha='center', va='center', 
                fontsize=10, style='italic')
    
    # Add arrows between layers
    for i in range(len(layers)-1):
        ax.annotate('', xy=(6, layers[i+1]['y']+0.4), xytext=(6, layers[i]['y']-0.4),
                   arrowprops=dict(arrowstyle='<->', lw=2, color='blue'))
    
    # Title and labels
    ax.set_title('System Architecture - 5-Layer Design', fontsize=16, fontweight='bold', pad=20)
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8.5)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/generated/system_architecture.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_development_metrics():
    """Figure 5.2 - Development Metrics Dashboard"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Code Statistics
    categories = ['Frontend\n(React)', 'Backend\n(Node.js)', 'Database\n(Oracle)', 'APIs\n(REST)']
    values = [25000, 20000, 87, 85]
    colors = ['#2196F3', '#4CAF50', '#FF9800', '#9C27B0']
    
    bars1 = ax1.bar(categories, values, color=colors)
    ax1.set_title('Code Statistics', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Count')
    
    # Add value labels on bars
    for bar, value in zip(bars1, values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}{"+" if value > 1000 else ""}',
                ha='center', va='bottom', fontweight='bold')
    
    # 2. Performance Metrics
    metrics = ['Response Time\n(ms)', 'Throughput\n(req/s)', 'Uptime\n(%)', 'Availability\n(%)']
    perf_values = [180, 1200, 99.95, 99.8]
    colors2 = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']
    
    bars2 = ax2.bar(metrics, perf_values, color=colors2)
    ax2.set_title('Performance Metrics', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Value')
    
    for bar, value in zip(bars2, perf_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}',
                ha='center', va='bottom', fontweight='bold')
    
    # 3. Usage Statistics
    usage_labels = ['Active Users', 'Prescriptions\nProcessed', 'Validations\nPerformed', 'Administrations\nRegistered']
    usage_values = [150, 8500, 7200, 15000]
    colors3 = ['#FF5722', '#607D8B', '#795548', '#3F51B5']
    
    bars3 = ax3.bar(usage_labels, usage_values, color=colors3)
    ax3.set_title('Usage Statistics', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Count')
    
    for bar, value in zip(bars3, usage_values):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}+',
                ha='center', va='bottom', fontweight='bold')
    
    # 4. Quality Metrics
    quality_labels = ['Concurrent\nUsers', 'Response\nTime <200ms', 'System\nUptime', 'Overall\nAvailability']
    quality_values = [500, 95, 99.95, 99.95]
    colors4 = ['#E91E63', '#00BCD4', '#8BC34A', '#FFC107']
    
    bars4 = ax4.bar(quality_labels, quality_values, color=colors4)
    ax4.set_title('Quality Metrics', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Value')
    
    for bar, value in zip(bars4, quality_values):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}%' if value < 100 else f'{value}+',
                ha='center', va='bottom', fontweight='bold')
    
    plt.suptitle('Development and Performance Metrics', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/development_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_error_reduction_dashboard():
    """Figure 5.3 - Error Reduction Analysis"""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # 1. Error Reduction Comparison
    error_types = ['Prescription\nErrors', 'Validation\nErrors', 'Administration\nErrors', 'Adverse\nEvents']
    reduction_percentages = [73, 85, 61, 45]
    colors = ['#f44336', '#FF9800', '#4CAF50', '#2196F3']
    
    bars1 = ax1.bar(error_types, reduction_percentages, color=colors)
    ax1.set_title('Error Reduction by Type', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Reduction Percentage (%)')
    ax1.set_ylim(0, 100)
    
    # Add percentage labels
    for bar, value in zip(bars1, reduction_percentages):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
                f'{value}%',
                ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    # Add horizontal line at 50% for reference
    ax1.axhline(y=50, color='red', linestyle='--', alpha=0.7, label='50% Target')
    ax1.legend()
    
    # 2. Time Efficiency Improvements
    time_categories = ['Prescription\nTime', 'Medication\nPreparation', 'Pharmacy\nValidation', 'Hospital\nDischarge']
    time_reductions = [35, 38, 50, 22]
    colors2 = ['#9C27B0', '#607D8B', '#795548', '#FF5722']
    
    bars2 = ax2.bar(time_categories, time_reductions, color=colors2)
    ax2.set_title('Time Efficiency Improvements', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Time Reduction (%)')
    ax2.set_ylim(0, 60)
    
    # Add percentage labels
    for bar, value in zip(bars2, time_reductions):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{value}%',
                ha='center', va='bottom', fontweight='bold', fontsize=12)
    
    # Add horizontal line at 30% for reference
    ax2.axhline(y=30, color='green', linestyle='--', alpha=0.7, label='30% Target')
    ax2.legend()
    
    plt.suptitle('Error Reduction and Time Efficiency Dashboard', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/error_reduction_dashboard.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_user_satisfaction_analysis():
    """Figure 5.4 - User Satisfaction Analysis"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Overall Satisfaction Scores
    metrics = ['SUS Score', 'Ease of Use', 'Overall\nSatisfaction', 'Learning\nTime Reduction']
    scores = [78, 8.7, 8.3, 65]
    max_scores = [100, 10, 10, 100]
    colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0']
    
    bars1 = ax1.bar(metrics, scores, color=colors)
    ax1.set_title('System Usability Metrics', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Score')
    
    # Add score labels
    for bar, score, max_score in zip(bars1, scores, max_scores):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{score}{"%" if max_score == 100 else ""}/{max_score}',
                ha='center', va='bottom', fontweight='bold')
    
    # 2. Professional Satisfaction by Role
    roles = ['Doctors', 'Pharmacists', 'Nurses', 'Administrators']
    satisfaction = [95, 92, 81, 88]
    colors2 = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12']
    
    bars2 = ax2.bar(roles, satisfaction, color=colors2)
    ax2.set_title('Professional Satisfaction by Role', fontsize=14, fontweight='bold')
    ax2.set_ylabel('Satisfaction (%)')
    ax2.set_ylim(0, 100)
    
    for bar, value in zip(bars2, satisfaction):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{value}%',
                ha='center', va='bottom', fontweight='bold')
    
    # 3. Communication Improvements
    comm_aspects = ['Doctor-\nPharmacist', 'Prescription\nClarity', 'Care\nCoordination']
    improvements = [60, 80, 45]
    colors3 = ['#9b59b6', '#1abc9c', '#e67e22']
    
    bars3 = ax3.bar(comm_aspects, improvements, color=colors3)
    ax3.set_title('Communication Improvements', fontsize=14, fontweight='bold')
    ax3.set_ylabel('Improvement (%)')
    
    for bar, value in zip(bars3, improvements):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{value}%',
                ha='center', va='bottom', fontweight='bold')
    
    # 4. System Comparison (Before vs After)
    comparison_data = {
        'Before': [4.2, 45, 35],
        'After': [8.7, 78, 65]
    }
    
    x = np.arange(3)
    width = 0.35
    
    bars_before = ax4.bar(x - width/2, comparison_data['Before'], width, label='Before', color='#e74c3c', alpha=0.7)
    bars_after = ax4.bar(x + width/2, comparison_data['After'], width, label='After', color='#2ecc71', alpha=0.7)
    
    ax4.set_title('System Comparison: Before vs After', fontsize=14, fontweight='bold')
    ax4.set_ylabel('Score')
    ax4.set_xticks(x)
    ax4.set_xticklabels(['Ease of Use\n(1-10)', 'SUS Score\n(0-100)', 'Learning Time\nReduction (%)'])
    ax4.legend()
    
    # Add value labels
    for bars in [bars_before, bars_after]:
        for bar in bars:
            height = bar.get_height()
            ax4.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}',
                    ha='center', va='bottom', fontweight='bold')
    
    plt.suptitle('User Satisfaction and System Usability Analysis', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/user_satisfaction.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_roi_analysis():
    """Figure 5.5 - ROI and Cost-Benefit Analysis"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # 1. Investment vs Savings
    categories = ['Total Investment', 'Annual Savings', 'Error Reduction\nSavings', 'Efficiency\nSavings']
    values = [280000, 450000, 450000, 180000]
    colors = ['#e74c3c', '#2ecc71', '#3498db', '#f39c12']
    
    bars1 = ax1.bar(categories, values, color=colors)
    ax1.set_title('Investment vs Savings (EUR)', fontsize=14, fontweight='bold')
    ax1.set_ylabel('Amount (EUR)')
    
    # Format values in thousands
    for bar, value in zip(bars1, values):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'€{value//1000}k',
                ha='center', va='bottom', fontweight='bold')
    
    # 2. ROI Timeline
    months = ['Month 1', 'Month 6', 'Month 8', 'Month 12', 'Month 18']
    roi_values = [-100, -40, 0, 60, 161]
    colors2 = ['#e74c3c' if x < 0 else '#2ecc71' for x in roi_values]
    
    bars2 = ax2.bar(months, roi_values, color=colors2)
    ax2.set_title('ROI Timeline (%)', fontsize=14, fontweight='bold')
    ax2.set_ylabel('ROI (%)')
    ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    
    for bar, value in zip(bars2, roi_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + (2 if height > 0 else -8),
                f'{value}%',
                ha='center', va='bottom' if height > 0 else 'top', fontweight='bold')
    
    # 3. Cost Breakdown
    cost_labels = ['Development', 'Implementation', 'Training', 'Infrastructure']
    cost_values = [180000, 60000, 25000, 15000]
    colors3 = ['#9b59b6', '#1abc9c', '#e67e22', '#34495e']
    
    wedges, texts, autotexts = ax3.pie(cost_values, labels=cost_labels, colors=colors3, autopct='%1.1f%%')
    ax3.set_title('Cost Breakdown', fontsize=14, fontweight='bold')
    
    # 4. Payback Period
    months_payback = np.arange(1, 13)
    cumulative_savings = np.cumsum([37500] * 12)  # 450k/12 months
    investment_line = [280000] * 12
    
    ax4.plot(months_payback, cumulative_savings, 'g-', linewidth=3, label='Cumulative Savings')
    ax4.plot(months_payback, investment_line, 'r--', linewidth=2, label='Initial Investment')
    ax4.fill_between(months_payback, cumulative_savings, investment_line, 
                    where=(cumulative_savings >= investment_line), 
                    color='green', alpha=0.3, label='Profit Zone')
    
    ax4.set_title('Payback Period Analysis', fontsize=14, fontweight='bold')
    ax4.set_xlabel('Months')
    ax4.set_ylabel('Amount (EUR)')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    # Mark breakeven point
    ax4.axvline(x=8, color='blue', linestyle=':', linewidth=2, label='Breakeven (8 months)')
    ax4.text(8.5, 300000, '8 months\nBreakeven', ha='left', va='center', 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))
    
    plt.suptitle('ROI and Cost-Benefit Analysis', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('images/generated/roi_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_future_roadmap():
    """Figure 5.6 - Future Development Roadmap"""
    fig, ax = plt.subplots(figsize=(14, 8))
    
    # Timeline data
    phases = [
        {'phase': 'Phase 1: AI Integration', 'start': 0, 'duration': 6, 'color': '#3498db'},
        {'phase': 'Phase 2: HL7 FHIR', 'start': 3, 'duration': 4, 'color': '#2ecc71'},
        {'phase': 'Phase 3: Mobile App', 'start': 6, 'duration': 5, 'color': '#e74c3c'},
        {'phase': 'Phase 4: Analytics', 'start': 9, 'duration': 3, 'color': '#f39c12'},
        {'phase': 'Phase 5: Expansion', 'start': 12, 'duration': 6, 'color': '#9b59b6'}
    ]
    
    # Draw timeline
    for i, phase in enumerate(phases):
        ax.barh(i, phase['duration'], left=phase['start'], height=0.6, 
                color=phase['color'], alpha=0.7, edgecolor='black')
        
        # Add phase label
        ax.text(phase['start'] + phase['duration']/2, i, phase['phase'], 
                ha='center', va='center', fontweight='bold', color='white')
    
    # Add features for each phase
    features = [
        ['Machine Learning', 'Predictive Analytics', 'Drug Interaction AI'],
        ['Full FHIR Compliance', 'National Interoperability', 'Data Standards'],
        ['Native Mobile App', 'Bedside Administration', 'Offline Capability'],
        ['Advanced Dashboards', 'Predictive Insights', 'Real-time Alerts'],
        ['3 New Hospitals', 'Regional Integration', 'Specialty Extensions']
    ]
    
    for i, feature_list in enumerate(features):
        feature_text = '\n'.join([f'• {feature}' for feature in feature_list])
        ax.text(18, i, feature_text, ha='left', va='center', fontsize=10,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))
    
    # Timeline labels
    ax.set_xlim(0, 25)
    ax.set_ylim(-0.5, len(phases) - 0.5)
    ax.set_xlabel('Timeline (Months)', fontsize=12)
    ax.set_yticks(range(len(phases)))
    ax.set_yticklabels([f'Phase {i+1}' for i in range(len(phases))])
    ax.set_title('Future Development Roadmap', fontsize=16, fontweight='bold')
    ax.grid(True, axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('images/generated/future_roadmap.png', dpi=300, bbox_inches='tight')
    plt.close()

def main():
    """Generate all results diagrams"""
    print("Generating Results chapter diagrams...")
    
    create_system_architecture()
    print("✓ Figure 5.1 - System Architecture")
    
    create_development_metrics()
    print("✓ Figure 5.2 - Development Metrics")
    
    create_error_reduction_dashboard()
    print("✓ Figure 5.3 - Error Reduction Dashboard")
    
    create_user_satisfaction_analysis()
    print("✓ Figure 5.4 - User Satisfaction Analysis")
    
    create_roi_analysis()
    print("✓ Figure 5.5 - ROI Analysis")
    
    create_future_roadmap()
    print("✓ Figure 5.6 - Future Development Roadmap")
    
    print("\nAll Results diagrams generated successfully!")

if __name__ == "__main__":
    main() 