import boto3
#Crear aws cli, aws accounts, and roles iam,
def iam_get_account_details():
    client = boto3.client('iam')
    response = client.get_account_authorization_details()
    return response

def iam_list_users():
    client = boto3.client('iam')
    users = client.list_users()
    return users  


client = boto3.client('iam')
paginator = client.get_paginator('get_account_authorization_details')

userList = list(paginator.paginate(Filter=['User']))
if userList[0]['IsTruncated'] == True:                  #TODO: need to properly handle truncated results
    print(Fore.RED+ "Truncated User List" + Fore.RESET)
groupList = list(paginator.paginate(Filter=['Group']))
if groupList[0]['IsTruncated'] == True:
    print(Fore.RED+ "Truncated Group List" + Fore.RESET)


for user in userList[0]['UserDetailList']:
    user_inline_policies = client.list_user_policies(UserName=user['UserName'])
    if user_inline_policies['IsTruncated'] == True:
        print(Fore.RED + "Truncated Inline Policies" + Fore.RESET)      # Prints whether or not results are truncated.
    
    #Get user inline policies
    print(Fore.BLUE + "User Name: ", user['UserName'] + Fore.RESET)     # Prints Username
    if len(user_inline_policies['PolicyNames']) == 0:
        print(Fore.LIGHTGREEN_EX +" - No Inline Policies found for", user['UserName'] + Fore.RESET)
    else:
        print(" - User Inline Policies: ", user_inline_policies['PolicyNames'])
        for user_inline_policy in user_inline_policies['PolicyNames']:
            inline_policy_document = client.get_user_policy(UserName=user['UserName'],PolicyName=user_inline_policy)
            print("           + Policy Statement for Inline Policy:" , Fore.LIGHTBLUE_EX + user_inline_policy + Fore.RESET)
            inline_policy_statement = inline_policy_document['PolicyDocument']['Statement']
            if type(inline_policy_statement) == type(dict()):
                for key,value in inline_policy_statement.items():   
                    if key == 'Action':                   #Prints all actions in separate lines
                        for j in inline_policy_statement['Action']:
                            print("              ", key, ":", j)
                    else:
                        print("              ", key, ":", value)      #Print all elements within the statement dictionary
            else:
                for statement in inline_policy_statement:       
                    for key,value in statement.items():      
                        print("              ", key, ":", value)
            print("\n", end="")

    #Get user managed policies        
    user_managed_policies = user.get('AttachedManagedPolicies')
    if len(user_managed_policies) == 0:
        print(Fore.LIGHTGREEN_EX +" - No Managed Policies found for", user['UserName'] + Fore.RESET)
    else:
        print(" - User Managed Policies:")
        for policy in user_managed_policies:
            user_managed_policy_arn = policy['PolicyArn']
            user_managed_policy_name = policy['PolicyName']
            user_managed_policy_details = client.get_policy(PolicyArn=user_managed_policy_arn)
            user_managed_policy_version = user_managed_policy_details['Policy']['DefaultVersionId']
            print(Fore.LIGHTBLUE_EX + "    +", user_managed_policy_name + Fore.RESET)
            print("    + Policy Statement for Managed User Policy:", Fore.LIGHTBLUE_EX + user_managed_policy_name + Fore.RESET)
            user_managed_policy_doc = client.get_policy_version(PolicyArn=user_managed_policy_arn, VersionId=user_managed_policy_version)
            for statement in user_managed_policy_doc['PolicyVersion']['Document']['Statement']:
                for k,v in statement.items():
                    if k == 'Action':
                        for action in statement['Action']:
                            print("              ", k, ":", action)
                    else:
                        print("              ", k, ":", v)
                print("\n", end="")

    #Get user group membership
    if len(user['GroupList']) == 0:
        print(Fore.LIGHTGREEN_EX + " - No Group Membership found for", user['UserName'], "\n" + Fore.RESET)
    else:
        print(" - User Group Membership: ", user.get('GroupList'))
        for group in user['GroupList']:
            for groupname in groupList[0]['GroupDetailList']:
                if groupname['GroupName'] == group:
                    print("     - Policies for Group:", Fore.RED + groupname['GroupName'] + Fore.RESET)
                    
                    # Inline Group Policies
                    if len(groupname['GroupPolicyList']) == 0:
                        print(Fore.LIGHTCYAN_EX + "        - No Inline Policies found"+ Fore.RESET)
                    else:
                        print(Fore.LIGHTCYAN_EX + "        - Inline policies: " + Fore.RESET)
                        for inlinepolicy in groupname['GroupPolicyList']:
                            inline_policy_name = inlinepolicy.get('PolicyName')
                            inline_policy_statement = client.get_group_policy(GroupName=group, PolicyName=inline_policy_name)
                            print(Fore.LIGHTBLUE_EX + "           +", inline_policy_name + Fore.RESET)
                            print("           + Policy Statement for Inline Policy:" , Fore.LIGHTBLUE_EX + inline_policy_name + Fore.RESET)
                            # print("           + ", inline_policy_statement['PolicyDocument']['Statement'])
                            for statement in inline_policy_statement['PolicyDocument']['Statement']:
                                for k,v in statement.items():
                                    if k == 'Action':                   #Prints all actions in separate lines
                                        for action in statement['Action']:
                                            print("              ", k, ":", action)
                                    else:
                                        print("              ", k, ":", v)      #Print all elements within the statement dictionary
                                print("\n", end="")
# Configurar cliente de AWS para NLB y GWLB
elbv2_client = boto3.client('elbv2', region_name='us-east-1')
network_firewall_client = boto3.client('network-firewall', region_name='us-east-1')

# Crear un Network Load Balancer (NLB)
response_nlb = elbv2_client.create_load_balancer(
    Name='MyNLB',
    Subnets=['subnet-12345678', 'subnet-87654321'],
    Scheme='internet-facing',
    Type='network',
    IpAddressType='ipv4',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyNLB'
        },
    ]
)

# Crear un Gateway Load Balancer (GWLB)
response_gwlb = network_firewall_client.create_firewall(
    FirewallName='MyGWLB',
    FirewallPolicyArn='arn:aws:network-firewall:us-east-1:123456789012:stateful-rule-group/applications/MyFirewallPolicy',
    VpcId='vpc-12345678',
    SubnetMappings=[
        {
            'SubnetId': 'subnet-12345678',
        },
        {
            'SubnetId': 'subnet-87654321',
        },
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyGWLB'
        },
    ]
)

# Imprimir las respuestas de creación
print("NLB creado:", response_nlb)
print("GWLB creado:", response_gwlb)
