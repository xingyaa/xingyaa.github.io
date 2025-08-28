#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
安全运营工作图生成器
Security Operations Work Diagram Generator
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

def create_security_operations_diagram():
    """创建安全运营工作图"""
    
    # 创建大尺寸画布
    fig, ax = plt.subplots(1, 1, figsize=(24, 16))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # 定义颜色方案
    colors = {
        'primary': '#2E86AB',      # 主蓝色
        'secondary': '#A23B72',    # 紫红色
        'accent': '#F18F01',       # 橙色
        'success': '#C73E1D',      # 红色
        'warning': '#FFB627',      # 黄色
        'info': '#87CEEB',         # 浅蓝色
        'light': '#F8F9FA',        # 浅灰色
        'dark': '#343A40'          # 深灰色
    }
    
    # 标题
    ax.text(50, 95, '安全运营工作全景图\nSecurity Operations Center (SOC) Overview', 
            fontsize=20, fontweight='bold', ha='center', va='center')
    
    # 核心安全运营模块
    core_modules = [
        # (x, y, width, height, title, color, details)
        (5, 75, 18, 15, '威胁情报管理\nThreat Intelligence', colors['primary'], 
         ['• 威胁情报收集', '• IOC管理', '• 威胁狩猎', '• 情报分析']),
        
        (27, 75, 18, 15, '安全监控\nSecurity Monitoring', colors['secondary'], 
         ['• SIEM/SOAR', '• 日志分析', '• 实时监控', '• 异常检测']),
        
        (49, 75, 18, 15, '事件响应\nIncident Response', colors['accent'], 
         ['• 事件分类', '• 应急处置', '• 取证分析', '• 恢复验证']),
        
        (71, 75, 18, 15, '漏洞管理\nVulnerability Management', colors['success'], 
         ['• 漏洞扫描', '• 风险评估', '• 补丁管理', '• 修复验证']),
    ]
    
    # 绘制核心模块
    for x, y, w, h, title, color, details in core_modules:
        # 主框
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", 
                             facecolor=color, alpha=0.8, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # 标题
        ax.text(x + w/2, y + h - 3, title, fontsize=12, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # 详细内容
        for i, detail in enumerate(details):
            ax.text(x + 1, y + h - 6 - i*2.5, detail, fontsize=9, 
                    ha='left', va='center', color='white')
    
    # 支撑体系
    support_systems = [
        # 左侧支撑
        (5, 50, 25, 20, '合规治理\nCompliance & Governance', colors['info'], 
         ['• 安全策略制定', '• 合规性检查', '• 风险评估', '• 审计管理', '• 安全培训', '• 制度流程']),
        
        # 右侧支撑  
        (70, 50, 25, 20, '安全工具平台\nSecurity Tools Platform', colors['warning'], 
         ['• 安全设备管理', '• 工具集成', '• 自动化编排', '• 数据分析', '• 报表展示', '• API管理']),
        
        # 中间核心
        (35, 50, 30, 20, '安全运营中心 (SOC)\nSecurity Operations Center', colors['dark'], 
         ['• 7×24小时监控', '• 安全分析师', '• 值班调度', '• 决策支持', '• 协调指挥', '• 知识库管理'])
    ]
    
    # 绘制支撑体系
    for x, y, w, h, title, color, details in support_systems:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.5", 
                             facecolor=color, alpha=0.7, edgecolor='black', linewidth=2)
        ax.add_patch(rect)
        
        # 标题
        ax.text(x + w/2, y + h - 3, title, fontsize=11, fontweight='bold', 
                ha='center', va='center', color='white' if color == colors['dark'] else 'black')
        
        # 详细内容
        text_color = 'white' if color == colors['dark'] else 'black'
        for i, detail in enumerate(details):
            ax.text(x + 1, y + h - 6 - i*2.2, detail, fontsize=8, 
                    ha='left', va='center', color=text_color)
    
    # 底层基础设施
    infrastructure = [
        (5, 20, 20, 25, '基础设施安全\nInfrastructure Security', colors['primary'], 
         ['网络安全:', '• 防火墙管理', '• IDS/IPS', '• 网络隔离', '• 流量分析', '', 
          '主机安全:', '• 终端防护', '• 服务器加固', '• 访问控制', '• 系统监控']),
        
        (30, 20, 20, 25, '数据安全\nData Security', colors['secondary'], 
         ['数据保护:', '• 数据分类', '• 加密管理', '• 备份策略', '• 访问审计', '', 
          '隐私保护:', '• 敏感数据识别', '• 数据脱敏', '• 权限管控', '• 合规检查']),
        
        (55, 20, 20, 25, '应用安全\nApplication Security', colors['accent'], 
         ['代码安全:', '• 静态代码扫描', '• 动态安全测试', '• 依赖检查', '• 安全开发', '', 
          '运行时保护:', '• WAF防护', '• API安全', '• 容器安全', '• 微服务安全']),
        
        (80, 20, 15, 25, '身份认证\nIdentity & Access', colors['success'], 
         ['身份管理:', '• 用户管理', '• 权限分配', '• SSO集成', '• 多因子认证', '', 
          '访问控制:', '• 零信任架构', '• 特权账号管理', '• 会话监控'])
    ]
    
    # 绘制基础设施模块
    for x, y, w, h, title, color, details in infrastructure:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.3", 
                             facecolor=color, alpha=0.6, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        
        # 标题
        ax.text(x + w/2, y + h - 2, title, fontsize=10, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # 详细内容
        for i, detail in enumerate(details):
            if detail and not detail.endswith(':'):
                ax.text(x + 0.5, y + h - 4.5 - i*1.8, detail, fontsize=7, 
                        ha='left', va='center', color='white')
            elif detail.endswith(':'):
                ax.text(x + 0.5, y + h - 4.5 - i*1.8, detail, fontsize=8, 
                        ha='left', va='center', color='yellow', fontweight='bold')
    
    # 绘制连接线 - 显示各模块间的关系
    connections = [
        # 核心模块间的连接
        ((14, 75), (27, 82)),  # 威胁情报 -> 监控
        ((45, 82), (49, 82)),  # 监控 -> 事件响应
        ((67, 82), (71, 82)),  # 事件响应 -> 漏洞管理
        
        # 核心模块到SOC的连接
        ((23, 75), (45, 70)),  # 威胁情报 -> SOC
        ((36, 75), (50, 70)),  # 监控 -> SOC
        ((58, 75), (55, 70)),  # 事件响应 -> SOC
        ((80, 75), (60, 70)),  # 漏洞管理 -> SOC
        
        # SOC到支撑体系的连接
        ((35, 60), (25, 65)),  # SOC -> 合规治理
        ((65, 60), (70, 65)),  # SOC -> 工具平台
        
        # 支撑体系到基础设施的连接
        ((17, 50), (15, 45)),  # 合规治理 -> 基础设施
        ((50, 50), (40, 45)),  # SOC -> 数据安全
        ((82, 50), (87, 45)),  # 工具平台 -> 身份认证
    ]
    
    for start, end in connections:
        arrow = ConnectionPatch(start, end, "data", "data", 
                              arrowstyle="->", shrinkA=5, shrinkB=5, 
                              mutation_scale=20, fc="gray", alpha=0.6)
        ax.add_patch(arrow)
    
    # 添加流程指示
    process_flow = [
        (5, 10, '1. 威胁检测', colors['primary']),
        (20, 10, '2. 事件分析', colors['secondary']),
        (35, 10, '3. 响应处置', colors['accent']),
        (50, 10, '4. 修复验证', colors['success']),
        (65, 10, '5. 持续改进', colors['warning']),
        (80, 10, '6. 知识积累', colors['info'])
    ]
    
    for x, y, text, color in process_flow:
        circle = plt.Circle((x + 7, y + 3), 2, color=color, alpha=0.8)
        ax.add_patch(circle)
        ax.text(x + 7, y + 3, text.split('.')[0], fontsize=10, fontweight='bold', 
                ha='center', va='center', color='white')
        ax.text(x + 7, y - 1, text.split('.')[1], fontsize=8, 
                ha='center', va='center', color='black')
    
    # 添加流程箭头
    for i in range(len(process_flow) - 1):
        start_x = process_flow[i][0] + 9
        end_x = process_flow[i + 1][0] + 5
        arrow = patches.FancyArrowPatch((start_x, 13), (end_x, 13),
                                      connectionstyle="arc3", 
                                      arrowstyle='->', mutation_scale=15, 
                                      color='gray', alpha=0.7)
        ax.add_patch(arrow)
    
    # 添加图例
    legend_items = [
        ('核心运营模块', colors['primary']),
        ('支撑体系', colors['info']),
        ('基础设施', colors['secondary']),
        ('运营流程', 'gray')
    ]
    
    for i, (label, color) in enumerate(legend_items):
        rect = plt.Rectangle((2, 2 - i*1.5), 1, 1, facecolor=color, alpha=0.8)
        ax.add_patch(rect)
        ax.text(4, 2.5 - i*1.5, label, fontsize=9, va='center')
    
    plt.tight_layout()
    return fig

def create_detailed_process_diagram():
    """创建详细的安全运营流程图"""
    
    fig, ax = plt.subplots(1, 1, figsize=(20, 14))
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    
    # 标题
    ax.text(50, 95, '安全运营详细流程图\nDetailed Security Operations Process Flow', 
            fontsize=18, fontweight='bold', ha='center', va='center')
    
    # 定义流程步骤
    processes = [
        # 第一层：检测和发现
        (10, 80, 15, 8, '威胁检测\nThreat Detection', '#FF6B6B', 
         ['• 日志监控', '• 异常检测', '• 威胁情报匹配']),
        (35, 80, 15, 8, '事件触发\nEvent Triggering', '#4ECDC4', 
         ['• 告警生成', '• 事件分类', '• 优先级排序']),
        (60, 80, 15, 8, '初步分析\nInitial Analysis', '#45B7D1', 
         ['• 事件验证', '• 影响评估', '• 分类标记']),
        
        # 第二层：分析和响应
        (10, 60, 15, 8, '深度分析\nDeep Analysis', '#96CEB4', 
         ['• 取证调查', '• 攻击链分析', '• 关联分析']),
        (35, 60, 15, 8, '响应决策\nResponse Decision', '#FFEAA7', 
         ['• 响应策略', '• 资源调配', '• 时间规划']),
        (60, 60, 15, 8, '执行响应\nExecute Response', '#DDA0DD', 
         ['• 遏制措施', '• 根除威胁', '• 系统恢复']),
        
        # 第三层：恢复和改进
        (10, 40, 15, 8, '损害评估\nDamage Assessment', '#F8B500', 
         ['• 影响范围', '• 数据损失', '• 业务影响']),
        (35, 40, 15, 8, '系统恢复\nSystem Recovery', '#20B2AA', 
         ['• 服务恢复', '• 数据恢复', '• 功能验证']),
        (60, 40, 15, 8, '事后分析\nPost-Incident Analysis', '#FF69B4', 
         ['• 总结报告', '• 经验教训', '• 改进建议']),
        
        # 第四层：持续改进
        (22.5, 20, 15, 8, '流程优化\nProcess Improvement', '#32CD32', 
         ['• 流程更新', '• 工具改进', '• 培训强化']),
        (47.5, 20, 15, 8, '知识管理\nKnowledge Management', '#FF7F50', 
         ['• 知识库更新', '• 最佳实践', '• 威胁情报更新'])
    ]
    
    # 绘制流程框
    for x, y, w, h, title, color, details in processes:
        rect = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.2", 
                             facecolor=color, alpha=0.8, edgecolor='black', linewidth=1.5)
        ax.add_patch(rect)
        
        # 标题
        ax.text(x + w/2, y + h - 1.5, title, fontsize=10, fontweight='bold', 
                ha='center', va='center', color='white')
        
        # 详细内容
        for i, detail in enumerate(details):
            ax.text(x + 0.5, y + h - 3 - i*1.2, detail, fontsize=8, 
                    ha='left', va='center', color='white')
    
    # 绘制流程箭头
    flow_arrows = [
        # 第一层横向连接
        ((25, 84), (35, 84)),
        ((50, 84), (60, 84)),
        
        # 第一层到第二层
        ((17.5, 80), (17.5, 68)),
        ((42.5, 80), (42.5, 68)),
        ((67.5, 80), (67.5, 68)),
        
        # 第二层横向连接
        ((25, 64), (35, 64)),
        ((50, 64), (60, 64)),
        
        # 第二层到第三层
        ((17.5, 60), (17.5, 48)),
        ((42.5, 60), (42.5, 48)),
        ((67.5, 60), (67.5, 48)),
        
        # 第三层横向连接
        ((25, 44), (35, 44)),
        ((50, 44), (60, 44)),
        
        # 第三层到第四层
        ((25, 40), (30, 28)),
        ((50, 40), (55, 28)),
        
        # 第四层横向连接
        ((37.5, 24), (47.5, 24))
    ]
    
    for start, end in flow_arrows:
        arrow = patches.FancyArrowPatch(start, end,
                                      connectionstyle="arc3,rad=0", 
                                      arrowstyle='->', mutation_scale=15, 
                                      color='darkblue', alpha=0.7, linewidth=2)
        ax.add_patch(arrow)
    
    # 添加阶段标签
    stages = [
        (85, 84, '检测发现阶段\nDetection Phase'),
        (85, 64, '分析响应阶段\nAnalysis & Response'),
        (85, 44, '恢复评估阶段\nRecovery & Assessment'),
        (85, 24, '改进学习阶段\nImprovement & Learning')
    ]
    
    for x, y, label in stages:
        ax.text(x, y, label, fontsize=11, fontweight='bold', 
                ha='center', va='center', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='lightgray', alpha=0.8))
    
    plt.tight_layout()
    return fig

if __name__ == "__main__":
    # 生成主要的安全运营工作图
    print("正在生成安全运营工作全景图...")
    fig1 = create_security_operations_diagram()
    fig1.savefig('/workspace/security_operations_overview.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print("安全运营工作全景图已保存为: security_operations_overview.png")
    
    # 生成详细流程图
    print("正在生成安全运营详细流程图...")
    fig2 = create_detailed_process_diagram()
    fig2.savefig('/workspace/security_operations_process.png', dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    print("安全运营详细流程图已保存为: security_operations_process.png")
    
    print("\n图表生成完成！")
    print("1. security_operations_overview.png - 安全运营工作全景图")
    print("2. security_operations_process.png - 安全运营详细流程图")