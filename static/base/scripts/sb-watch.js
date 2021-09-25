'use strict';

const _ = require('lodash');
const chokidar = require('chokidar');
const dotenv = require('dotenv');
const plimit = require('p-limit');
const renderAssets = require('./render-assets');
const renderScripts = require('./render-scripts');
const renderSCSS = require('./render-scss');
const upath = require('upath');
const workerpool = require('workerpool');

const pool = workerpool.pool(__dirname + '/render-pug.js', {
    minWorkers: 'max',
});

const parsedENV = dotenv.config().parsed || {};

const watcher = chokidar.watch('src', {
    persistent: true,
});

let READY = false;

process.title = 'pug-watch';
process.stdout.write('Loading');
let allPugFiles = {};

watcher.on('add', filePath => _processFile(upath.normalize(filePath), 'add'));
watcher.on('change', filePath => _processFile(upath.normalize(filePath), 'change'));
watcher.on('ready', () => {
    READY = true;
    console.log(' READY TO ROLL!');
});

_handleSCSS();

function _processFile(filePath, watchEvent) {
    
    if (!READY) {
        if (filePath.match(/\.pug$/)) {
            if (!filePath.match(/includes/) && !filePath.match(/mixins/) && !filePath.match(/\/pug\/layouts\//)) {
                allPugFiles[filePath] = true;
            }    
        }    
        process.stdout.write('.');
        return;
    }

    console.log(`### INFO: File event: ${watchEvent}: ${filePath}`);

    if (filePath.match(/\.pug$/)) {
        return _handlePug(filePath, watchEvent);
    }

    if (filePath.match(/\.scss$/)) {
        if (watchEvent === 'change') {
            return _handleSCSS(filePath, watchEvent);
        }
        return;
    }

    if (filePath.match(/src\/js\//)) {
        return renderScripts();
    }

    if (filePath.match(/src\/assets\//)) {
        return renderAssets();
    }

}

function _handlePug(filePath, watchEvent) {
    if (watchEvent === 'change') {
        if (filePath.match(/includes/) || filePath.match(/mixins/) || filePath.match(/\/pug\/layouts\//)) {
            return _renderAllPug();
        }
        return _renderPug(filePath);
    }
    if (!filePath.match(/includes/) && !filePath.match(/mixins/) && !filePath.match(/\/pug\/layouts\//)) {
        return _renderPug(filePath);
    }
}

function _renderAllPug() {
    console.log('### INFO: Rendering All');
    const limit = plimit(parseInt(parsedENV.PARALLEL_PUG_RENDERS || '2', 10));
    const promiseArray = [];
    _.each(allPugFiles, (value, filePath) => promiseArray.push(limit(() => _renderPug(filePath))));
    Promise.all(promiseArray);
}

function _handleSCSS() {
    renderSCSS();
}

function _renderPug(filePath) {
    return new Promise(function (resolve, reject) {
        pool.exec('renderPug', [filePath])
            .then(function (result) {
                resolve(result);
            })
            .catch(function (err) {
                console.error(err);
                reject(err);
            });
    });
}
