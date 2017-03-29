node('dko-personal') {
    def image
    stage('Build') {
        echo 'Building..'
        checkout scm
        sh """
            # Get an unique venv folder to using *inside* workspace
            VENV=".venv-$BUILD_NUMBER"

            # Initialize new venv
            virtualenv "$VENV"

            # Update pip
            PS1="${PS1:-}" source "$VENV/bin/activate"

            #install requirements
            pip install -r requirements.txt
            python manage.py migrate    # Apply South's database migrations
            python manage.py compilemessages          # Create translation files
            python manage.py collectstatic --noinput  # Collect static files
        """
    }
    stage('Test') {
        sh """
            PS1="${PS1:-}" source "$VENV/bin/activate"
            python manage.py test --noinput
        """
    }
    stage('Deploy') {
        if (! fileExists '/webapps/$JOB_NAME') {
            sh '''
                mkdir -p "/webapps/$JOB_NAME"
                virtualenv "/webapps/$JOB_NAME/.venv"
            '''
        } else {
            dir('/webapps/$JOB_NAME') {
                sh '''
                    tar cfv "../archive_$JOB_NAME-$BUILD_NUMBER" ./
                    rm -rf ./*
                '''
            }
        }
        dir('/webapps/$JOB_NAME') {
            // some block
            git 'https://github.com/dejwoo/xp_project'
            sh '''
                PS1="${PS1:-}" source "/webapps/$JOB_NAME/.venv/bin/activate"
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
