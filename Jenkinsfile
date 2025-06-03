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
                        ssh -o StrictHostKeyChecking=no ubuntu@3.83.116.192 <<EOF
                            rm -rf flask-app || true
                            git clone https://github.com/ssptr007/flask-app.git flask-app
                            cd flask-app
                            pkill -f app.py
                            nohup python3 app.py > app.log 2>&1 &
                        EOF
                    '''
                }
            }
        }
    }
}
