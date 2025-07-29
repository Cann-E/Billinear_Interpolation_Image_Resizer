pipeline {
    agent { docker { image 'pmantini/assignment-cosc6380:latest' } }

    environment {
        PATH = "env/bin/:$PATH"
    }
    stages {
        stage('build') {
            steps {
                sh 'python dip_hw1_resize.py -i cell2.jpg -fx 0.75 -fy 0.75 -m nearest_neighbor > output/resize/1/output1.txt'
                sh 'python dip_hw1_resize.py -i cell2.jpg -fx 1.25 -fy 1.25 -m nearest_neighbor > output/resize/1/output2.txt'
                sh 'python dip_hw1_resize.py -i cells.png -fx 1.25 -fy 1.25 -m nearest_neighbor > output/resize/2/output1.txt'
                sh 'python dip_hw1_resize.py -i cells.png -fx 1.25 -fy 1.25 -m bilinear > output/resize/2/output2.txt'   
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'output/**/*.* ', onlyIfSuccessful: true
        }
    }
}
