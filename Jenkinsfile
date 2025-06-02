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
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                nohup python3 app.py &
            EOF
            '''
        }
    }
}
