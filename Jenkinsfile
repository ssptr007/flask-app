pipeline {
    agent any

    stages {
        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result.toString() == 'SUCCESS' }
            }
            steps {
                sshagent(['ec2-key-jenkins']) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ubuntu@3.83.116.192 bash -s <<'ENDSSH'
                            set -e
                            rm -rf /home/ubuntu/flask-app || true
                            git clone https://github.com/ssptr007/flask-app.git /home/ubuntu/flask-app
                            cd /home/ubuntu/flask-app
                            pkill -f app.py || true
                            nohup python3 app.py > app.log 2>&1 &
                        ENDSSH
                    """
                }
            }
        }
    }
}
