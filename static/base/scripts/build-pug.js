'use strict';
const dotenv = require('dotenv');
const plimit = require('p-limit');
const sh = require('shelljs');
const upath = require('upath');
const workerpool = require('workerpool');

const parsedENV = dotenv.config().parsed || {};
const srcPath = upath.resolve(upath.dirname(__filename), '../src');
const pool = workerpool.pool(__dirname + '/render-pug.js', {
    minWorkers: 'max',
});

const limit = plimit(parseInt(parsedENV.PARALLEL_PUG_RENDERS || '2', 10));
const promiseArray = [];

for (const path of sh.find(srcPath)) {
    promiseArray.push(limit(() => _processFile(path)));
}

Promise.all(promiseArray).then(() => {
    pool.terminate();
});

function _processFile(filePath) {
    if (
        filePath.match(/\.pug$/) &&
        !filePath.match(/include/) &&
        !filePath.match(/mixin/) &&
        !filePath.match(/\/pug\/layouts\//)
    ) {
        return _renderPug(filePath);
    }
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
