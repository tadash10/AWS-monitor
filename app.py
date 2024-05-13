from flask import Flask, render_template
import boto3

app = Flask(__name__)

# Initialize AWS clients
iam_client = boto3.client('iam')
ec2_client = boto3.client('ec2')
cloudwatch_client = boto3.client('cloudwatch')
cloudtrail_client = boto3.client('cloudtrail')
ssm_client = boto3.client('ssm')

@app.route('/')
def dashboard():
    # Get some information from AWS
    iam_roles = iam_client.list_roles()['Roles']
    ec2_instances = ec2_client.describe_instances()['Reservations']
    cloudtrail_trails = cloudtrail_client.describe_trails()['trailList']
    
    return render_template('dashboard.html', iam_roles=iam_roles, ec2_instances=ec2_instances, cloudtrail_trails=cloudtrail_trails)

if __name__ == '__main__':
    app.run(debug=True)
