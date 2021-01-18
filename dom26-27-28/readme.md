1.Создать ansible роль для установки nginx, в роли должен быть шаблон nginx.conf.j2 (в темплейте должны быть for, if и default значения)

Для установки nginx на удаленные машины с системами Ubuntu и CentOS, испльзовать playbook.yml Listing:

---
- name: Inst NGINX 
  hosts: prod
  become: yes
    
  roles:
   - deploy_nginx_web





2.Разобраться с модулем docker для ansible
