pipeline {
    agent { label 'windows' }

    options {
        buildDiscarder(logRotator(numToKeepStr: '30'))
        disableConcurrentBuilds()
    }

    environment {
        UE_ROOT      = "C:/Program Files/Epic Games/UE_5.6"
        PROJECT_PATH = "${WORKSPACE}/Greedy_Piggies.uproject"
        UE_CONFIG    = "Development"
        BUILD_DIR    = "BuildOutput"
        ZIP_DIR      = "Builds"
        ZIP_NAME     = "Greedy_Piggies_Win64_${BUILD_NUMBER}.zip"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'staging',
                    url: 'https://github.com/University-for-the-Creative-Arts/Greedy_Piggies',
                    credentialsId: 'Github'
            }
        }

        stage('Sanity Check') {
            steps {
                bat """
                if not exist "%UE_ROOT%/Engine/Build/BatchFiles/RunUAT.bat" exit /b 2
                if not exist "%PROJECT_PATH%" exit /b 3
                """
            }
        }

        stage('Build Unreal Project') {
            steps {
                bat """
                "%UE_ROOT%/Engine/Build/BatchFiles/RunUAT.bat" ^
                  BuildCookRun ^
                  -project="%PROJECT_PATH%" ^
                  -noP4 ^
                  -platform=Win64 ^
                  -clientconfig=%UE_CONFIG% ^
                  -build -cook -stage -pak -archive ^
                  -archivedirectory="%WORKSPACE%/%BUILD_DIR%"
                """
            }
        }

    }
}