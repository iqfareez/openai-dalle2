![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# [Dall•E 2](https://openai.com/dall-e-2/) (OpenAI Image Generation)

## Getting started

1. Register yourself for [OpenAI](https://beta.openai.com/) account. Check if there is any free grant is given, if not, setup a paid account.
2. Get API key from https://beta.openai.com/account/api-keys
3. Create a file called `.env` in the root of the project and add the following line:

   ```
   OPENAI_API_KEY=<your api key>
   ```

4. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

5. In `main.py` file, modify the `prompt` variable to your liking
6. Run the script:

   ```
   py main.py
   ```

7. The generated image URLs will be printed out in the terminal. You can open it in your browser to see the result

## Example results

| Prompt                                                 | Generated image                             |
| ------------------------------------------------------ | ------------------------------------------- |
| `A realistic image of a boss cat doing work in office` | ![result1](https://i.imgur.com/kMCLkUO.png) |
| `A digital art of a lighthouse and andromeda galaxy`   | ![Result2](https://i.imgur.com/yPvoSJS.png) |
| `Realistic image of human civilization on a mars`      | ![Result3](https://i.imgur.com/ncWoOSX.png) |
| `A depiction of life in year 3040`                     | ![Result4](https://i.imgur.com/MvTSVam.png) |
