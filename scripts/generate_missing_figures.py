#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar figuras em falta do capítulo Resultados
Figuras: ROI Analysis e Future Roadmap
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import seaborn as sns
from datetime import datetime, timedelta

# Set style for academic presentation
plt.style.use('default')
sns.set_palette("husl")

def create_roi_analysis():
    """Figure 5.5 - ROI Analysis Dashboard"""
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # ROI Timeline
    months = np.arange(1, 25)
    investment = np.array([280000] * 24)
    cumulative_savings = np.cumsum([0] + [37500] * 23)
    net_roi = cumulative_savings - investment
    
    ax1.plot(months, net_roi, 'b-', linewidth=2, label='Net ROI')
    ax1.axhline(y=0, color='r', linestyle='--', alpha=0.7)
    ax1.fill_between(months, net_roi, 0, where=(net_roi > 0), alpha=0.3, color='green', label='Positive ROI')
    ax1.fill_between(months, net_roi, 0, where=(net_roi <= 0), alpha=0.3, color='red', label='Negative ROI')
    ax1.set_xlabel('Months')
    ax1.set_ylabel('Net ROI (EUR)')
    ax1.set_title('ROI Timeline Analysis')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Cost Breakdown
    costs = [280000, 450000, 180000, 120000]
    labels = ['Initial Investment', 'Error Reduction\nSavings', 'Efficiency\nSavings', 'Maintenance\nCosts']
    colors = ['red', 'green', 'blue', 'orange']
    
    ax2.bar(labels, costs, color=colors, alpha=0.7)
    ax2.set_ylabel('Amount (EUR)')
    ax2.set_title('Cost-Benefit Breakdown')
    ax2.tick_params(axis='x', rotation=45)
    
    # Payback Period
    payback_months = np.arange(1, 13)
    monthly_savings = 37500
    cumulative_payback = np.cumsum([monthly_savings] * 12)
    
    ax3.plot(payback_months, cumulative_payback, 'g-', linewidth=2, marker='o')
    ax3.axhline(y=280000, color='r', linestyle='--', label='Initial Investment')
    ax3.fill_between(payback_months, cumulative_payback, 280000, 
                    where=(cumulative_payback >= 280000), alpha=0.3, color='green')
    ax3.set_xlabel('Months')
    ax3.set_ylabel('Cumulative Savings (EUR)')
    ax3.set_title('Payback Period Analysis')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    
    # Key Metrics
    metrics = ['ROI (%)', 'Payback (months)', 'NPV (EUR)', 'IRR (%)']
    values = [161, 8, 650000, 24]
    
    bars = ax4.bar(metrics, values, color=['darkgreen', 'blue', 'purple', 'orange'], alpha=0.7)
    ax4.set_ylabel('Values')
    ax4.set_title('Key Financial Metrics')
    
    # Add value labels on bars
    for bar, value in zip(bars, values):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height,
                f'{value}', ha='center', va='bottom', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('images/generated/roi_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_future_roadmap():
    """Figure 5.6 - Future Development Roadmap"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Roadmap phases
    phases = [
        {'name': 'Phase 1: AI Implementation', 'start': 0, 'duration': 6, 'color': 'red'},
        {'name': 'Phase 2: HL7 FHIR Integration', 'start': 3, 'duration': 8, 'color': 'blue'},
        {'name': 'Phase 3: Mobile App Development', 'start': 6, 'duration': 10, 'color': 'green'},
        {'name': 'Phase 4: Predictive Analytics', 'start': 12, 'duration': 6, 'color': 'orange'},
        {'name': 'Phase 5: Regional Expansion', 'start': 18, 'duration': 12, 'color': 'purple'},
        {'name': 'Phase 6: Full Interoperability', 'start': 24, 'duration': 8, 'color': 'brown'},
    ]
    
    # Plot phases
    for i, phase in enumerate(phases):
        y_pos = i * 0.8
        ax.barh(y_pos, phase['duration'], left=phase['start'], height=0.6, 
                color=phase['color'], alpha=0.7, label=phase['name'])
        
        # Add phase text
        ax.text(phase['start'] + phase['duration']/2, y_pos, phase['name'], 
                ha='center', va='center', fontweight='bold', color='white')
    
    # Add milestones
    milestones = [
        {'name': 'ML Models Ready', 'month': 6, 'y': 0},
        {'name': 'FHIR Standards Compliant', 'month': 11, 'y': 0.8},
        {'name': 'Mobile App Beta', 'month': 16, 'y': 1.6},
        {'name': 'Analytics Dashboard', 'month': 18, 'y': 2.4},
        {'name': '3 Hospitals Live', 'month': 30, 'y': 3.2},
        {'name': 'National Integration', 'month': 32, 'y': 4.0},
    ]
    
    for milestone in milestones:
        ax.scatter(milestone['month'], milestone['y'], s=100, color='black', zorder=5)
        ax.annotate(milestone['name'], (milestone['month'], milestone['y']), 
                   xytext=(10, 10), textcoords='offset points', 
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                   fontsize=8, fontweight='bold')
    
    # Add timeline
    ax.set_xlim(0, 36)
    ax.set_ylim(-0.5, 5)
    ax.set_xlabel('Timeline (Months)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Development Phases', fontsize=12, fontweight='bold')
    ax.set_title('Future Development Roadmap\nSystem Expansion and Enhancement Strategy', 
                 fontsize=14, fontweight='bold')
    
    # Customize y-axis
    ax.set_yticks([i * 0.8 for i in range(len(phases))])
    ax.set_yticklabels([f'Phase {i+1}' for i in range(len(phases))])
    
    # Add grid
    ax.grid(True, axis='x', alpha=0.3)
    
    # Add legend for key technologies
    legend_elements = [
        mpatches.Patch(color='red', label='AI/ML Technologies'),
        mpatches.Patch(color='blue', label='Interoperability Standards'),
        mpatches.Patch(color='green', label='Mobile Solutions'),
        mpatches.Patch(color='orange', label='Advanced Analytics'),
        mpatches.Patch(color='purple', label='System Expansion'),
        mpatches.Patch(color='brown', label='Full Integration')
    ]
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
    
    plt.tight_layout()
    plt.savefig('images/generated/future_roadmap.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating missing figures...")
    
    # Create ROI Analysis figure
    create_roi_analysis()
    print("✓ ROI Analysis figure created: images/generated/roi_analysis.png")
    
    # Create Future Roadmap figure
    create_future_roadmap()
    print("✓ Future Roadmap figure created: images/generated/future_roadmap.png")
    
    print("\nAll missing figures generated successfully!") 