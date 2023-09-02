import ipaddress

from colors import colors

def show_name_of_program():
      print(f"""{colors.red}  
            
          
        ____         _ _                                   _                         _        
       / ___|_   _(_) | |__   ___ _ __ _ __ ___   ___     / \  _   _  __ _ _   _ ___| |_ ___  
      | |  _| | | | | | '_ \ / _ \ '__| '_ ` _ \ / _ \   / _ \| | | |/ _` | | | / __| __/ _ \ 
      | |_| | |_| | | | | | |  __/ |  | | | | | |  __/  / ___ \ |_| | (_| | |_| \__ \ || (_) |
       \____|\__,_|_|_|_| |_|\___|_|  |_| |_| |_|\___| /_/   \_\__,_|\__, |\__,_|___/\__\___/ 
                                                                     |___/                    
            __     ___                  ____      _            _       _             
            \ \   / / |___ _ __ ___    / ___|__ _| | ___ _   _| | __ _| |_ ___  _ __ 
             \ \ / /| / __| '_ ` _ \  | |   / _` | |/ __| | | | |/ _` | __/ _ \| '__|
              \ V / | \__ \ | | | | | | |__| (_| | | (__| |_| | | (_| | || (_) | |   
               \_/  |_|___/_| |_| |_|  \____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
            
            
          
            
            {colors.reset}""")


def calcular_vlsm(ip_rede, num_hosts):
    try:
        rede = ipaddress.ip_network(ip_rede, strict=False)
        subnets = list(rede.subnets(new_prefix=32 - num_hosts.bit_length()))
        for subnet in subnets:
            print(f"{colors.orange}Rede: {subnet.network_address}{colors.reset}")
            print(f"{colors.orange}Broadcast: {subnet.broadcast_address}{colors.reset}")
            print(f"{colors.orange}Máscara: {subnet.netmask} /{subnet.prefixlen}{colors.reset}")
            print(f"{colors.green}IPs válidos:{colors.reset}")
            for ip in list(subnet.hosts()):
                print(f"{colors.green}{str(ip).ljust(15)}   Máscara: {subnet.netmask} /{subnet.prefixlen}{colors.reset}")
            print()
            print(f"{colors.green}{'-'*74}{colors.reset}")
            print()
    except ValueError:
        print(f"{colors.red}Endereço IP inválido. Por favor, insira um endereço IP válido.{colors.reset}")



    show_name_of_program()
    
    ip_rede = input(f'{colors.orange}Digite o endereço IP da rede (ex: 192.168.0.0/24): {colors.reset}')
    num_hosts = int(input(f'{colors.orange}Digite a quantidade de hosts que deseja suportar: {colors.reset}'))

    calcular_vlsm(ip_rede, num_hosts)



