product = "test"  # 项目名称
user = 'test'  # 用户目录
configs = {
    'base_file': "base.log",
    'bbs_path': "/home/www/htdocs/html/bbs.{0}.iccgame.com/".format(product),
    'bak_dir': "/home/{0}/bbs_bak/".format(user),
    'logs_path': "forumdata/logs/{0}/{1}.log",
    'ip_deny_file': '/usr/local/nginx/conf/Configs/deny-ip-bbs.conf',  # 需要在对应网站的配置文件include导入此文件
    'web_server': "service nginxd restart",
}