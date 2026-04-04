import boto3

def create_ec2_instance(ami_id, size, MyEC2Instance007):
    ec2 = boto3.resource('ec2')
    instance = ec2.create_instances(
        ImageId= ami_id,
        InstanceType=size,
        MinCount=1,
        MaxCount=1,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': MyEC2Instance007
                    }
                ]
            }
        ]

    )
    print(f'Created EC2 instance with ID: {instance[0].id}')

create_ec2_instance('ami-0ca7038e6ff499fc0', 't2.micro', 'MyEC2Instance007')    