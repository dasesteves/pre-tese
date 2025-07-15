#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para gerar um diagrama de Gantt detalhado para a pré-tese.
Mapeia as fases do projeto ao longo de 12 meses (Nov 2024 - Out 2025).
"""

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def create_detailed_gantt_chart():
    """Gera o diagrama de Gantt detalhado para o projeto da tese."""
    fig, ax = plt.subplots(figsize=(16, 10))

    # Definir as tarefas, datas de início e durações
    # Datas baseadas num cronograma de 12 meses que termina em Outubro de 2025
    tasks = {
        "Phase 1: Research & Definition": [
            ("1.1: Literature Review", "2024-11-01", 60),
            ("1.2: Process Mapping @ SCMVV", "2024-12-01", 30),
            ("1.3: Stakeholder Interviews", "2025-01-01", 30),
            ("1.4: Requirements Elicitation (SRS)", "2025-01-15", 45),
            ("1.5: System Architecture Design", "2025-02-15", 30),
        ],
        "Phase 2: Core Development": [
            ("2.1: Setup Environments", "2025-03-01", 15),
            ("2.2: Database & Core Data Layer", "2025-03-15", 45),
            ("2.3: Authentication & Security Module", "2025-04-15", 30),
            ("2.4: e-Prescription Module (Backend)", "2025-05-01", 45),
            ("2.5: Pharmacy & Validation Module (Backend)", "2025-06-01", 45),
        ],
        "Phase 3: Integration & Testing": [
            ("3.1: Unit & Integration Testing", "2025-05-15", 75),
            ("3.2: Performance Optimization", "2025-06-15", 45),
            ("3.3: External System Integrations", "2025-07-15", 45),
        ],
        "Phase 4: Pilot & Evaluation": [
            ("4.1: Pilot Deployment @ SCMVV", "2025-07-15", 15),
            ("4.2: User Training & Onboarding", "2025-07-20", 25),
            ("4.3: Data Collection & Feedback", "2025-08-01", 60),
            ("4.4: Final System Refinements", "2025-09-01", 30),
        ],
        "Phase 5: Dissertation & Submission": [
            ("5.1: Results Analysis & Discussion", "2025-09-01", 30),
            ("5.2: Full Dissertation Writing", "2025-09-01", 50),
            ("5.3: Final Review & Submission", "2025-10-10", 15),
            ("5.4: Defense Preparation", "2025-10-15", 10),
        ],
    }

    y_pos = []
    task_labels = []
    start_dates = []
    durations = []
    
    # Processar tarefas para o gráfico
    current_y = 0
    phase_colors = plt.cm.viridis(np.linspace(0, 1, len(tasks)))
    task_colors = []

    for i, (phase, task_list) in enumerate(tasks.items()):
        # Adicionar a barra da fase
        phase_start = datetime.strptime(task_list[0][1], "%Y-%m-%d")
        phase_end = datetime.strptime(task_list[-1][1], "%Y-%m-%d") + timedelta(days=task_list[-1][2])
        phase_duration = (phase_end - phase_start).days
        
        ax.barh(current_y + 0.5, phase_duration, left=phase_start, height=0.5, 
                color=phase_colors[i], alpha=0.3, edgecolor='black', label=phase)
        ax.text(phase_start + timedelta(days=2), current_y + 0.5, phase, 
                va='center', ha='left', color='black', fontweight='bold', fontsize=12)

        current_y -= (len(task_list) + 1)
        
        # Adicionar as tarefas individuais
        for task_name, start, duration in reversed(task_list):
            y_pos.append(current_y + len(task_list) * 0.5)
            task_labels.append(task_name)
            start_date = datetime.strptime(start, "%Y-%m-%d")
            start_dates.append(start_date)
            durations.append(timedelta(days=duration))
            task_colors.append(phase_colors[i])
        current_y += (len(task_list))


    ax.barh(y_pos, durations, left=start_dates, height=0.5, align='center', 
            color=task_colors, alpha=0.8, edgecolor='black')

    # Formatação do gráfico
    ax.set_yticks(y_pos)
    ax.set_yticklabels(task_labels)
    ax.invert_yaxis()  # As tarefas no topo primeiro

    # Formatar o eixo X para mostrar meses
    ax.xaxis_date()
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45)

    # Adicionar grelha e título
    ax.grid(True, which='major', axis='x', linestyle='--', alpha=0.6)
    ax.set_xlabel("Timeline (Months)", fontweight='bold')
    ax.set_ylabel("Project Tasks", fontweight='bold')
    ax.set_title("Detailed Project Gantt Chart (Nov 2024 - Oct 2025)", fontsize=16, fontweight='bold')
    
    # Adicionar linha do dia de hoje para referência (se dentro do intervalo)
    today = datetime.now()
    if datetime(2024, 11, 1) < today < datetime(2025, 10, 31):
        ax.axvline(today, color='red', linestyle='-', linewidth=2, label='Today')

    # Melhorar layout e salvar
    fig.tight_layout()
    plt.savefig('images/generated/gantt_chart_detailed.png', dpi=300)
    plt.close()
    print("✓ Diagrama de Gantt detalhado gerado: images/generated/gantt_chart_detailed.png")


if __name__ == "__main__":
    # O numpy pode ser necessário para `linspace`
    try:
        import numpy as np
    except ImportError:
        print("Aviso: A biblioteca 'numpy' não está instalada. A geração de cores pode falhar.")
        print("Execute: pip install numpy")
    
    print("Gerando o diagrama de Gantt detalhado...")
    create_detailed_gantt_chart()
    print("Processo concluído!") 