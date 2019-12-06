#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 2019/12/6 7:36 PM
"""
alert_config = {
    "Watchdog": {
        "name": "监控正常检查",
        "description": "如果收到该告警，表示监控告警链路正常",
        "runbook": "如果收到该告警，表示监控正常"
    },
    # 应用
    "KubeDeploymentGenerationMismatch": {
        "name": "应用实例版本不匹配",
        "description": "应用实例数量长时间未升级完成,目前处于老版本",
        "runbook": "请查看应用实例状态，请根据容器日志和监控信息排查原因"
    },
    "KubeDeploymentReplicasMismatch": {
        "name": "应用实例数量长时间未达到指定数量异常",
        "description": "应用实例数量长时间未达到指定数量异常,请查看应用实例状态，排查原因",
        "runbook": "应用实例数量长时间未达到指定数量异常,请查看应用实例状态，排查原因，可能是应用升级失败，资源不足，应用配置错误等原因"
    },
    "KubePodCrashTooManyTimes": {
        "name": "容器重启多次异常",
        "description": "容器因未知原因已重启多次，请根据容器日志和监控信息排查原因",
        "runbook": "容器因未知原因已重启多次，请根据容器日志和监控信息排查原因"
    },
    "KubePodCrashTooManyTimesApp": {
        "name": "容器重启多次异常",
        "description": "容器因未知原因已重启多次，请根据容器日志和监控信息排查原因",
        "runbook": "容器因未知原因已重启多次，请根据容器日志和监控信息排查原因"
    },
    "KubePodCrashLooping": {
        "name": "容器异常退出",
        "description": "容器异常退出，请根据容器日志和监控信息排查原因",
        "runbook": "容器异常退出，请根据容器日志和监控信息排查原因"
    },
    "KubePodNotReady": {
        "name": "容器监控检查失败异常",
        "description": "容器监控检查失败异常，路由处于端口状态",
        "runbook": "请根据容器监控检查配置信息排查失败原因"
    },
    # 运维
    "KubeNodeNotReady": {
        "name": "集群节点状态异常",
        "description": "集群节点状态异常,控制节点无法连接到该节点",
        "runbook": "请检查集群网络状态,节点是否因系统或硬件等原因异常关机等"
    },
    "NodeFilesystemAlmostOutOfFiles": {
        "name": "集群节点磁盘inode数量满异常",
        "description": "集群节点磁盘可用inode数量少于5%,请尽快处理",
        "runbook": "请检查集群节点inode使用情况(df -i),然后进一步排查是那个应用在大量写小文件,选择合适方式处理"
    },
    "NodeFilesystemAlmostOutOfSpace": {
        "name": "集群节点磁盘空间满异常",
        "description": "集群节点磁盘空间数量少于5%,请尽快处理",
        "runbook": "请检查集群节点空间使用情况(df -h),进行扩容或者清理磁盘"
    },

    "NodeFilesystemFilesFillingUp": {
        "name": "集群节点磁盘inode数量增加速度异常",
        "description": "文件系统inode将在接下来的24小时内耗尽,请尽快处理",
        "runbook": "请检查集群节点inode使用情况(df -i),然后进一步排查是那个应用在大量写小文件,选择合适方式处理"
    },
    "NodeFilesystemSpaceFillingUp": {
        "name": "集群节点磁盘空间量满增加速度异常",
        "description": "集群节点磁盘空间将在接下来的24小时内耗尽,请尽快处理",
        "runbook": "请检查集群节点空间使用情况(df -h),进行扩容或者清理磁盘"
    },
    "ClockSkewDetected": {
        "name": "集群时间同步异常",
        "description": "集群时间同步异常,请尽快处理",
        "runbook": "请检查集群时间同步软件状态,确保集群内节点时间同步"
    },
    "default": {
        "name": "K8S 集群检测到未知异常请排查",
        "description": "K8S 集群检测到未知异常请登录alertmanger排查",
        "runbook": "K8S 集群检测到未知异常请登录alertmanger排查"
    }
}