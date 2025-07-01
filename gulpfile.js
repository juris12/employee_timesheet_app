const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));

function compileSass() {
    return gulp.src([
        'employees/static/employees/scss/**/*.scss', 
        'static/scss/**/*.scss'
    ])
        .pipe(sass().on('error', sass.logError))
        .pipe(gulp.dest(function(file) {
            return file.base.replace('scss', 'css');
        }));
}

function watch() {
    gulp.watch([
        'employees/static/employees/scss/**/*.scss',
        'static/scss/**/*.scss'
    ], compileSass);
}

// Exports
exports.compileSass = compileSass;
exports.watch = watch;