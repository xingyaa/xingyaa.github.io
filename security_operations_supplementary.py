#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安全运营指标和工具清单图
Security Operations Metrics and Tools Chart
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

# 设置字体
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_metrics_and_tools_diagram():
    """创建安全运营指标和工具清单图"""
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(24, 16))
    
    # 颜色方案
    colors = {
        'metrics': '#3498db',
        'tools': '#e74c3c',
        'processes': '#2ecc71',
        'kpis': '#f39c12',
        'light': '#ecf0f1',
        'dark': '#34495e'
    }
    
    # 第一象限：关键绩效指标 (KPIs)
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.set_title('Security Operations KPIs\nKey Performance Indicators', 
                  fontsize=16, fontweight='bold', pad=20)
    ax1.axis('off')
    
    kpis = [
        ('MTTD', 'Mean Time To Detection', '8.2 hours', '#e74c3c'),
        ('MTTR', 'Mean Time To Response', '2.5 hours', '#3498db'),
        ('MTBF', 'Mean Time Between Failures', '720 hours', '#2ecc71'),
        ('Uptime', 'System Availability', '99.95%', '#f39c12'),
        ('FPR', 'False Positive Rate', '< 5%', '#9b59b6'),
        ('Coverage', 'Security Coverage', '94%', '#1abc9c'),
        ('SOC Efficiency', 'Incident Closure Rate', '98%', '#e67e22'),
        ('Compliance', 'Audit Success Rate', '100%', '#34495e')
    ]
    
    y_pos = 9.5
    for i, (metric, description, value, color) in enumerate(kpis):
        # 创建指标框
        rect = FancyBboxPatch((0.5, y_pos-0.8), 9, 0.7, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, alpha=0.8)
        ax1.add_patch(rect)
        
        # 添加文本
        ax1.text(1, y_pos-0.45, f"{metric}: {value}", 
                fontsize=12, fontweight='bold', color='white')
        ax1.text(1, y_pos-0.65, description, 
                fontsize=9, color='white', alpha=0.9)
        
        y_pos -= 1.1
    
    # 第二象限：安全工具栈
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.set_title('Security Tools Stack\nTechnology Infrastructure', 
                  fontsize=16, fontweight='bold', pad=20)
    ax2.axis('off')
    
    tool_categories = [
        ('SIEM/SOAR', ['Splunk', 'QRadar', 'Phantom', 'Demisto'], '#e74c3c'),
        ('Endpoint', ['CrowdStrike', 'Carbon Black', 'Sentinel One'], '#3498db'),
        ('Network', ['Firewall', 'IDS/IPS', 'DLP', 'Proxy'], '#2ecc71'),
        ('Vulnerability', ['Nessus', 'Qualys', 'OpenVAS', 'Rapid7'], '#f39c12'),
        ('Cloud Security', ['CASB', 'CWPP', 'CSPM', 'CloudTrail'], '#9b59b6'),
        ('Threat Intel', ['MISP', 'ThreatConnect', 'Anomali'], '#1abc9c')
    ]
    
    y_start = 9.5
    for category, tools, color in tool_categories:
        # 类别标题
        rect = FancyBboxPatch((0.5, y_start-0.4), 9, 0.3, 
                             boxstyle="round,pad=0.05", 
                             facecolor=color, alpha=0.9)
        ax2.add_patch(rect)
        ax2.text(5, y_start-0.25, category, fontsize=11, fontweight='bold', 
                ha='center', color='white')
        
        # 工具列表
        tool_text = ' • '.join(tools)
        ax2.text(1, y_start-0.7, tool_text, fontsize=9, color=color, 
                fontweight='bold')
        
        y_start -= 1.5
    
    # 第三象限：安全运营流程矩阵
    ax3.set_xlim(0, 10)
    ax3.set_ylim(0, 10)
    ax3.set_title('Security Operations Process Matrix\nProcess Integration', 
                  fontsize=16, fontweight='bold', pad=20)
    ax3.axis('off')
    
    # 创建流程矩阵
    processes = ['Detection', 'Analysis', 'Response', 'Recovery', 'Learning']
    phases = ['Prevention', 'Detection', 'Response', 'Recovery']
    
    # 绘制矩阵网格
    for i, process in enumerate(processes):
        for j, phase in enumerate(phases):
            x = 1.5 + j * 1.8
            y = 8.5 - i * 1.5
            
            # 计算成熟度级别 (示例数据)
            maturity = np.random.choice([1, 2, 3, 4, 5])
            color_intensity = maturity / 5.0
            
            rect = Rectangle((x, y), 1.6, 1.2, 
                           facecolor=plt.cm.RdYlGn(color_intensity), 
                           alpha=0.8, edgecolor='black')
            ax3.add_patch(rect)
            
            # 添加成熟度级别
            ax3.text(x + 0.8, y + 0.6, str(maturity), 
                    fontsize=14, fontweight='bold', ha='center', va='center')
    
    # 添加标签
    for i, process in enumerate(processes):
        ax3.text(0.5, 9.1 - i * 1.5, process, fontsize=10, fontweight='bold', 
                ha='right', va='center')
    
    for j, phase in enumerate(phases):
        ax3.text(2.3 + j * 1.8, 9.8, phase, fontsize=10, fontweight='bold', 
                ha='center', va='bottom', rotation=0)
    
    # 添加图例
    legend_y = 2
    ax3.text(1, legend_y, 'Maturity Scale:', fontsize=10, fontweight='bold')
    for level in range(1, 6):
        color_intensity = level / 5.0
        rect = Rectangle((2.5 + (level-1) * 0.8, legend_y - 0.3), 0.6, 0.4, 
                        facecolor=plt.cm.RdYlGn(color_intensity), 
                        alpha=0.8, edgecolor='black')
        ax3.add_patch(rect)
        ax3.text(2.8 + (level-1) * 0.8, legend_y - 0.1, str(level), 
                fontsize=9, ha='center', va='center', fontweight='bold')
    
    # 第四象限：威胁情报和事件统计
    ax4.set_xlim(0, 10)
    ax4.set_ylim(0, 10)
    ax4.set_title('Threat Intelligence & Incident Statistics\nSecurity Metrics Dashboard', 
                  fontsize=16, fontweight='bold', pad=20)
    ax4.axis('off')
    
    # 威胁类型分布饼图区域
    threat_data = [25, 20, 18, 15, 12, 10]
    threat_labels = ['Malware', 'Phishing', 'DDoS', 'Data Breach', 'Insider', 'Other']
    threat_colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7', '#dda0dd']
    
    # 创建小型饼图
    pie_center = (2.5, 7.5)
    pie_radius = 1.2
    
    # 计算角度
    angles = []
    start_angle = 0
    for value in threat_data:
        angle = (value / sum(threat_data)) * 360
        angles.append((start_angle, angle))
        start_angle += angle
    
    # 绘制饼图扇形
    for i, ((start, angle), label, color) in enumerate(zip(angles, threat_labels, threat_colors)):
        wedge = patches.Wedge(pie_center, pie_radius, start, start + angle, 
                            facecolor=color, alpha=0.8, edgecolor='white', linewidth=2)
        ax4.add_patch(wedge)
        
        # 添加标签
        mid_angle = np.radians(start + angle/2)
        label_x = pie_center[0] + (pie_radius + 0.3) * np.cos(mid_angle)
        label_y = pie_center[1] + (pie_radius + 0.3) * np.sin(mid_angle)
        ax4.text(label_x, label_y, f'{label}\n{threat_data[i]}%', 
                fontsize=8, ha='center', va='center', fontweight='bold')
    
    # 事件严重级别统计
    severity_stats = [
        ('Critical', 15, '#e74c3c'),
        ('High', 45, '#f39c12'),
        ('Medium', 120, '#f1c40f'),
        ('Low', 280, '#2ecc71'),
        ('Info', 540, '#3498db')
    ]
    
    bar_x = 6
    bar_width = 0.6
    max_incidents = max([count for _, count, _ in severity_stats])
    
    ax4.text(6.5, 9, 'Monthly Incidents by Severity', 
            fontsize=12, fontweight='bold', ha='center')
    
    for i, (severity, count, color) in enumerate(severity_stats):
        y_pos = 8 - i * 1.2
        bar_height = 0.8
        bar_length = (count / max_incidents) * 3
        
        # 绘制条形图
        rect = Rectangle((bar_x, y_pos), bar_length, bar_height, 
                        facecolor=color, alpha=0.8)
        ax4.add_patch(rect)
        
        # 添加标签
        ax4.text(bar_x - 0.1, y_pos + bar_height/2, severity, 
                fontsize=10, ha='right', va='center', fontweight='bold')
        ax4.text(bar_x + bar_length + 0.1, y_pos + bar_height/2, str(count), 
                fontsize=10, ha='left', va='center', fontweight='bold')
    
    # 添加时间趋势信息
    trend_info = [
        'Trends (Last 30 days):',
        '↗ Phishing attacks +15%',
        '↘ Malware incidents -8%',
        '→ DDoS attempts stable',
        '↗ Cloud threats +25%'
    ]
    
    y_trend = 3.5
    for info in trend_info:
        color = '#2c3e50' if info.startswith('Trends') else '#7f8c8d'
        weight = 'bold' if info.startswith('Trends') else 'normal'
        ax4.text(6, y_trend, info, fontsize=9, color=color, fontweight=weight)
        y_trend -= 0.4
    
    plt.tight_layout()
    return fig

def create_roles_responsibilities_diagram():
    """创建安全运营角色职责图"""
    
    fig, ax = plt.subplots(1, 1, figsize=(20, 12))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # 标题
    ax.text(50, 95, 'Security Operations Center - Roles & Responsibilities\nSOC Team Structure and Functions', 
            fontsize=18, fontweight='bold', ha='center', va='center')
    
    # 定义角色和职责
    roles = [
        # (x, y, width, height, title, responsibilities, color)
        (5, 75, 40, 18, 'SOC Manager / CISO\nSecurity Leadership', 
         ['• Strategic planning and governance', '• Resource allocation and budget', 
          '• Stakeholder communication', '• Policy and procedure development',
          '• Risk management oversight', '• Compliance and audit coordination'], '#34495e'),
        
        (55, 75, 40, 18, 'SOC Analyst L1 (Triage)\n24/7 Monitoring', 
         ['• Real-time alert monitoring', '• Initial event classification', 
          '• Basic incident documentation', '• Escalation to L2/L3 analysts',
          '• Tool maintenance and updates', '• Report generation'], '#3498db'),
        
        (5, 50, 40, 18, 'SOC Analyst L2 (Investigation)\nIncident Analysis', 
         ['• Deep dive incident analysis', '• Threat hunting and research', 
          '• Forensic evidence collection', '• Attack vector analysis',
          '• Containment recommendations', '• Playbook development'], '#e74c3c'),
        
        (55, 50, 40, 18, 'SOC Analyst L3 (Expert)\nAdvanced Response', 
         ['• Complex incident response', '• Malware reverse engineering', 
          '• Advanced threat analysis', '• Custom tool development',
          '• Threat intelligence analysis', '• Mentor junior analysts'], '#2ecc71'),
        
        (5, 25, 40, 18, 'Security Engineer\nInfrastructure & Tools', 
         ['• Security tool deployment', '• Integration and automation', 
          '• Performance optimization', '• Architecture design',
          '• Technical documentation', '• Vendor management'], '#f39c12'),
        
        (55, 25, 40, 18, 'Threat Intelligence Analyst\nThreat Research', 
         ['• Threat landscape monitoring', '• IOC collection and analysis', 
          '• Threat actor profiling', '• Intelligence sharing',
          '• Threat briefing preparation', '• Risk assessment support'], '#9b59b6'),
        
        (20, 5, 25, 12, 'Incident Response Team\nCrisis Management', 
         ['• Emergency response coordination', '• Cross-functional communication', 
          '• Business continuity support', '• Post-incident reviews'], '#1abc9c'),
        
        (55, 5, 25, 12, 'Compliance Officer\nRegulatory Oversight', 
         ['• Regulatory compliance monitoring', '• Audit preparation and support', 
          '• Policy compliance verification', '• Training coordination'], '#e67e22')
    ]
    
    # 绘制角色框
    for x, y, w, h, title, responsibilities, color in roles:
        # 主框
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", 
                             facecolor=color, alpha=0.8, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # 标题
        ax.text(x + w/2, y + h - 2, title, fontsize=12, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # 职责列表
        for i, responsibility in enumerate(responsibilities):
            ax.text(x + 1, y + h - 5 - i*2, responsibility, fontsize=9, 
                    ha='left', va='center', color='white')
    
    # 添加连接线显示汇报关系
    connections = [
        # SOC Manager connections
        ((25, 75), (35, 68)),  # Manager to L2
        ((25, 75), (75, 75)),  # Manager to L1
        ((25, 75), (25, 68)),  # Manager to Security Engineer
        
        # Analyst progression
        ((75, 75), (75, 68)),  # L1 to L2
        ((45, 60), (55, 60)),  # L2 to L3
        
        # Support connections
        ((75, 50), (75, 37)),  # L3 to Threat Intel
        ((25, 50), (32, 17)),  # L2 to IR Team
        ((45, 25), (55, 17)),  # Security Engineer to Compliance
    ]
    
    for start, end in connections:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color='gray', lw=2, alpha=0.7))
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    # 生成指标和工具图
    print("Generating Security Operations Metrics and Tools diagram...")
    fig1 = create_metrics_and_tools_diagram()
    fig1.savefig('/workspace/security_operations_metrics_tools.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print("Security Operations Metrics and Tools diagram saved as: security_operations_metrics_tools.png")
    
    # 生成角色职责图
    print("Generating SOC Roles and Responsibilities diagram...")
    fig2 = create_roles_responsibilities_diagram()
    fig2.savefig('/workspace/soc_roles_responsibilities.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print("SOC Roles and Responsibilities diagram saved as: soc_roles_responsibilities.png")
    
    print("\nAll supplementary diagrams generated successfully!")
    print("1. security_operations_metrics_tools.png - KPIs, Tools, Process Matrix")
    print("2. soc_roles_responsibilities.png - SOC Team Structure")