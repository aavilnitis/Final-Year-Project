const spawner = require('child_process').spawn;

const getEasyGame = async (req, res) => {
    try {
        const python_process = spawner('python3', ['backend/controllers/sudoku/python/sudoku_script_generate.py', JSON.stringify(0)]);
        let stdoutData = null;

        python_process.stderr.on('data', (data) => {
            console.error('Error from python: ' + data.toString());
        });

        python_process.stdout.on('data', (data) => {
            stdoutData = JSON.parse(data.toString());
        });

        python_process.on('close', (code) => {
            if (stdoutData) {
                res.status(200).json(stdoutData);
            } else {
                res.status(200).json({ message: 'No output from python script' });
            }
        });

    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const getMediumGame = async (req, res) => {
    try {
        const python_process = spawner('python3', ['backend/controllers/sudoku/python/sudoku_script_generate.py', JSON.stringify(1)]);
        let stdoutData = null;

        python_process.stderr.on('data', (data) => {
            console.error('Error from python: ' + data.toString());
        });

        python_process.stdout.on('data', (data) => {
            stdoutData = JSON.parse(data.toString());
        });

        python_process.on('close', (code) => {
            if (stdoutData) {
                res.status(200).json(stdoutData);
            } else {
                res.status(200).json({ message: 'No output from python script' });
            }
        });

    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const getHardGame = async (req, res) => {
    try {
        const python_process = spawner('python3', ['backend/controllers/sudoku/python/sudoku_script_generate.py', JSON.stringify(2)]);
        let stdoutData = null;

        python_process.stderr.on('data', (data) => {
            console.error('Error from python: ' + data.toString());
        });

        python_process.stdout.on('data', (data) => {
            stdoutData = JSON.parse(data.toString());
        });

        python_process.on('close', (code) => {
            if (stdoutData) {
                res.status(200).json(stdoutData);
            } else {
                res.status(200).json({ message: 'No output from python script' });
            }
        });

    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const solveGame = async (req, res) => {
    try {
        const game = req.body.sudoku_game;

        const python_process = spawner('python3', ['backend/controllers/sudoku/python/sudoku_script_solve.py', JSON.stringify(game)]);
        let stdoutData = null;

        python_process.stderr.on('data', (data) => {
            console.error('Error from python: ' + data.toString());
        });

        python_process.stdout.on('data', (data) => {
            stdoutData = JSON.parse(data.toString());
        });

        python_process.on('close', (code) => {
            if (stdoutData) {
                res.status(200).json(stdoutData);
            } else {
                res.status(200).json({ message: 'No output from python script' });
            }
        });

    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

module.exports = { getEasyGame, getMediumGame, getHardGame, solveGame };
