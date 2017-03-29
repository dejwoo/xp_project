node('dko-personal') {
    def image
    stage('Build') {
        echo 'Building..'
        checkout scm
        sh '''
            # Get an unique venv folder to using *inside* workspace
            VENV=".venv-$BUILD_NUMBER"

            # Initialize new venv
            virtualenv "$VENV"

            # Update pip
            PS1="${PS1:-}" . "$VENV/bin/activate"

            #install requirements
            pip install -r requirements.txt
            python manage.py migrate    # Apply Souths database migrations
            #python manage.py compilemessages          # Create translation files
            python manage.py collectstatic --noinput  # Collect static files
        '''
    }
    stage('Test') {
        sh '''
            VENV=".venv-$BUILD_NUMBER"
            PS1="${PS1:-}" . "$VENV/bin/activate"
            python manage.py test --noinput
        '''
    }
    stage('Deploy') {
        if (! fileExists("/webapps/$JOB_NAME")) {
            sh '''
                mkdir -p "/webapps/$JOB_NAME"
            '''
        } else {
            dir("/webapps/$JOB_NAME") {
                sh '''
                    tar cfv "../archive_$JOB_NAME-$BUILD_NUMBER.tar" ./
                    rm -rf ./*
                '''
            }
        }
        dir("/webapps/$JOB_NAME") {
            // some block
            checkout scm
            if (! fileExists('.venv')) {
                sh 'virtualenv .venv'
            }
            sh '''
                PS1="${PS1:-}" . ".venv/bin/activate"
                #install requirements
                pip install -r requirements.txt
                python manage.py migrate                  # Apply Souths database migrations
                python manage.py compilemessages          # Create translation files
                python manage.py collectstatic --noinput  # Collect static files
            '''
            echo "Please restart gunicorn & co"
        }
    }
}
