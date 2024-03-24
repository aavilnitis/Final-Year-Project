const fs = require('fs');
const path = require('path');

const spawner = require('child_process').spawn;

const solveGame = async (req, res) => {
    try {
        const row_args = req.body.row_args;
        const col_args = req.body.col_args;
        const game = [row_args, col_args]

        const python_process = spawner('python3', ['backend/controllers/nonogram/python/nonogram_script.py', JSON.stringify(game)]);
        let stdoutData = null;

        python_process.stderr.on('data', (data) => {
            console.error('Error from python: ' + data.toString());
        });

        python_process.stdout.on('data', (data) => {
            let parsedData = JSON.parse(data.toString());
            parsedData = parsedData.map(row => row.map(cell => cell === 1 ? 0 : 1));
            stdoutData = parsedData;
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

const getAllGames = async (req, res) => {
    try {
        // Directory where the JSON files are located
        const directoryPath = path.join(__dirname, './', 'games');
        // Array to store all rows and columns tuples
        let allGames = [];

        // Read all files in the directory
        fs.readdir(directoryPath, async (err, files) => {
            if (err) {
                throw err;
            }

            // Loop through each file
            for (const file of files) {
                // Read JSON file
                const filePath = path.join(directoryPath, file);
                const fileContent = fs.readFileSync(filePath);
                const jsonData = JSON.parse(fileContent);

                // Extract rows and columns from each game
                const games = jsonData.games;
                for (const game of games) {
                    const { rows, columns } = game;
                    allGames.push([rows, columns]);
                }
            }

            res.status(200).json(allGames);
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const getSmallGames = async (req, res) => {
    try {
        // File path for small_games.json
        const filePath = path.join(__dirname, './', 'games', 'small_games.json');

        // Read the content of the file
        const fileContent = fs.readFileSync(filePath, 'utf8');

        // Parse the JSON content
        const jsonData = JSON.parse(fileContent);

        // Extract rows and columns from the JSON data
        const games = jsonData.games;
        const allGames = games.map(game => [game.rows, game.columns]);

        // Send the rows and columns as response
        res.status(200).json(allGames);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const getMediumGames = async (req, res) => {
    try {
        // File path for medium_games.json
        const filePath = path.join(__dirname, './', 'games', 'medium_games.json');

        // Read the content of the file
        const fileContent = fs.readFileSync(filePath, 'utf8');

        // Parse the JSON content
        const jsonData = JSON.parse(fileContent);

        // Extract rows and columns from the JSON data
        const games = jsonData.games;
        const allGames = games.map(game => [game.rows, game.columns]);

        // Send the rows and columns as response
        res.status(200).json(allGames);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const getLargeGames = async (req, res) => {
    try {
        // File path for large_games.json
        const filePath = path.join(__dirname, './', 'games', 'large_games.json');

        // Read the content of the file
        const fileContent = fs.readFileSync(filePath, 'utf8');

        // Parse the JSON content
        const jsonData = JSON.parse(fileContent);

        // Extract rows and columns from the JSON data
        const games = jsonData.games;
        const allGames = games.map(game => [game.rows, game.columns]);

        // Send the rows and columns as response
        res.status(200).json(allGames);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

const getXlGames = async (req, res) => {
    try {
        // File path for xl_games.json
        const filePath = path.join(__dirname, './', 'games', 'xl_games.json');

        // Read the content of the file
        const fileContent = fs.readFileSync(filePath, 'utf8');

        // Parse the JSON content
        const jsonData = JSON.parse(fileContent);

        // Extract rows and columns from the JSON data
        const games = jsonData.games;
        const allGames = games.map(game => [game.rows, game.columns]);

        // Send the rows and columns as response
        res.status(200).json(allGames);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
};

module.exports = { solveGame, getAllGames, getSmallGames, getMediumGames, getLargeGames, getXlGames };
