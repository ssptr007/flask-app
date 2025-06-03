pipeline {
    agent any

    stages {
        stage('Deploy') {
            when {
                expression { currentBuild.result == null || currentBuild.result.toString() == 'SUCCESS' }
            }
            steps {
                sshagent(credentials: ['ec2-key-jenkins']) {
                    sh '''#!/bin/bash
                        ssh -o StrictHostKeyChecking=no ubuntu@3.83.116.192 << 'EOF'
                            set -e
                            rm -rf /home/ubuntu/flask-app || true
                            git clone https://github.com/ssptr007/flask-app.git flask-app
                            cd flask-app
                            pkill -f app.py || true
                            nohup python3 app.py > output.log 2>&1 &
                        EOF
                    '''
                }
            }
        }
    }
}
