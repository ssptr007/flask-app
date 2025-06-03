pipeline {
    agent any

    stages {
        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                sshagent(['ec2-key-jenkins']) {
                    sh '''
                        ssh -o StrictHostKeyChecking=no ubuntu@3.83.116.192 << 'ENDSSH'
                            rm -rf /home/ubuntu/flask-app || true
                            git clone https://github.com/ssptr007/flask-app.git /home/ubuntu/flask-app
                            cd /home/ubuntu/flask-app
                            pkill -f app.py || true
                            ssh ubuntu@3.83.116.192 << 'EOF'
                            
                            nohup python3 app.py &
                            EOF
                        ENDSSH
                    '''
                }
            }
        }
    }
}
