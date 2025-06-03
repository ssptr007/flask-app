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
                            echo "Cleaning up old app..."
                            pkill -f app.py || true
                            rm -rf /home/ubuntu/flask-app || true

                            echo "Cloning latest code..."
                            git clone https://github.com/ssptr007/flask-app.git /home/ubuntu/flask-app

                            cd /home/ubuntu/flask-app

                            echo "Starting app..."
                            nohup python3 app.py > app.log 2>&1 &
                        ENDSSH
                    '''
                }
            }
        }
    }
}
