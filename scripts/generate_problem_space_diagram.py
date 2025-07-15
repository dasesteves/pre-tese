#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to generate the problem space diagram for the Introduction chapter
Shows fragmented workflow and information silos in hospital medication management
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
import numpy as np

def create_problem_space_diagram():
    """Generate Figure 1.1 - Problem Space Diagram"""
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # Define colors
    colors = {
        'physician': '#e3f2fd',
        'pharmacist': '#f3e5f5', 
        'nurse': '#e8f5e9',
        'database': '#fff3e0',
        'problems': '#ffebee'
    }
    
    # Current Fragmented Workflow (Top section)
    workflow_y = 7.5
    
    # Physician box
    physician_box = FancyBboxPatch(
        (1, workflow_y), 3, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=colors['physician'],
        edgecolor='darkblue',
        linewidth=2
    )
    ax.add_patch(physician_box)
    ax.text(2.5, workflow_y + 0.75, 'Physician\n(Prescription System)', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Pharmacist box
    pharmacist_box = FancyBboxPatch(
        (6, workflow_y), 3, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=colors['pharmacist'],
        edgecolor='darkmagenta',
        linewidth=2
    )
    ax.add_patch(pharmacist_box)
    ax.text(7.5, workflow_y + 0.75, 'Pharmacist\n(Pharmacy System)', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Nurse box
    nurse_box = FancyBboxPatch(
        (11, workflow_y), 3, 1.5,
        boxstyle="round,pad=0.1",
        facecolor=colors['nurse'],
        edgecolor='darkgreen',
        linewidth=2
    )
    ax.add_patch(nurse_box)
    ax.text(12.5, workflow_y + 0.75, 'Nurse\n(Administration System)', 
            ha='center', va='center', fontsize=11, fontweight='bold')
    
    # Manual communication arrows
    # Physician to Pharmacist
    ax.annotate('', xy=(6, workflow_y + 0.75), xytext=(4, workflow_y + 0.75),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(5, workflow_y + 1.2, 'Manual/Delayed\nCommunication', 
            ha='center', va='center', fontsize=9, color='red', fontweight='bold')
    
    # Pharmacist to Nurse
    ax.annotate('', xy=(11, workflow_y + 0.75), xytext=(9, workflow_y + 0.75),
                arrowprops=dict(arrowstyle='->', lw=2, color='red'))
    ax.text(10, workflow_y + 1.2, 'Manual/Delayed\nCommunication', 
            ha='center', va='center', fontsize=9, color='red', fontweight='bold')
    
    # Information Silos (Middle section)
    silo_y = 5
    
    # Database boxes
    db_boxes = [
        {'name': 'Prescription\nDatabase', 'x': 1.5, 'color': colors['database']},
        {'name': 'Pharmacy\nDatabase', 'x': 6.5, 'color': colors['database']},
        {'name': 'Administration\nRecords', 'x': 11.5, 'color': colors['database']}
    ]
    
    for db in db_boxes:
        db_box = FancyBboxPatch(
            (db['x'], silo_y), 2, 1.2,
            boxstyle="round,pad=0.1",
            facecolor=db['color'],
            edgecolor='darkorange',
            linewidth=2
        )
        ax.add_patch(db_box)
        ax.text(db['x'] + 1, silo_y + 0.6, db['name'], 
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Arrows from workflow to databases
    arrow_positions = [(2.5, 6.5), (7.5, 11.5), (12.5, 16.5)]
    for i, (start_x, end_x) in enumerate([(2.5, 2.5), (7.5, 7.5), (12.5, 12.5)]):
        ax.annotate('', xy=(start_x, silo_y + 1.2), xytext=(start_x, workflow_y),
                    arrowprops=dict(arrowstyle='->', lw=2, color='gray'))
    
    # Resulting Problems (Bottom section)
    problems_y = 2.5
    
    problem_boxes = [
        {'name': 'Medication\nErrors', 'x': 2, 'color': colors['problems']},
        {'name': 'Process\nInefficiencies', 'x': 6.5, 'color': colors['problems']},
        {'name': 'Lack of\nTraceability', 'x': 11, 'color': colors['problems']}
    ]
    
    for prob in problem_boxes:
        prob_box = FancyBboxPatch(
            (prob['x'], problems_y), 2.5, 1,
            boxstyle="round,pad=0.1",
            facecolor=prob['color'],
            edgecolor='darkred',
            linewidth=2
        )
        ax.add_patch(prob_box)
        ax.text(prob['x'] + 1.25, problems_y + 0.5, prob['name'], 
                ha='center', va='center', fontsize=10, fontweight='bold')
    
    # Arrows from silos to problems
    for i, db in enumerate(db_boxes):
        for j, prob in enumerate(problem_boxes):
            start_x = db['x'] + 1
            end_x = prob['x'] + 1.25
            ax.annotate('', xy=(end_x, problems_y + 1), xytext=(start_x, silo_y),
                        arrowprops=dict(arrowstyle='->', lw=1, color='darkred', alpha=0.6))
    
    # Section labels
    ax.text(7.5, 9.5, 'Current Fragmented Workflow', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', alpha=0.8))
    
    ax.text(7.5, 6.5, 'Information Silos', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightyellow', alpha=0.8))
    
    ax.text(7.5, 1.5, 'Resulting Problems', 
            ha='center', va='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.3", facecolor='lightcoral', alpha=0.8))
    
    # Title
    ax.set_title('Problem Space: Fragmented Medication Management Workflow', 
                 fontsize=16, fontweight='bold', pad=20)
    
    # Remove axes
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10.5)
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig('images/generated/problem_space_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Problem space diagram generated: images/generated/problem_space_diagram.png")

if __name__ == "__main__":
    print("Generating problem space diagram...")
    create_problem_space_diagram()
    print("Diagram generation completed!") 