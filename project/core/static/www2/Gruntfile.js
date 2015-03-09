module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    sass: {
      options: {
        includePaths: ['bower_components/foundation/scss']
      },
      dev: {
        options: {
          outputStyle: 'expanded'
        },
        files: {
          'css/app.css': 'scss/app.scss'
        }
      },
      dist: {
        options: {
          outputStyle: 'compressed'
        },
        files: {
          'css/app.css': 'scss/app.scss'
        }
      }
    },
    watch: {
        sass: {
            files: ['scss/**/*.scss'],
            tasks: ['sass']
        }
    },
    browserSync: {
        dev: {
            bsFiles: {
                src: ['css/*.css','./*.html']
            }
        },
        options: {
            watchTask: true,
            reloadDelay: 500,
            server: {
                baseDir: './',
                index: 'index.html'
            },
            ghostMode: false,
            open: "external"
        }
    }
  });

  grunt.loadNpmTasks('grunt-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-browser-sync');

  grunt.registerTask('build', ['sass:dist']);
  grunt.registerTask('default', ['sass:dev','browserSync', 'watch']);
}
