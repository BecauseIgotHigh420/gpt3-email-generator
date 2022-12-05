import openai
import os

class ml_backend:

    os.environ["OPENAI_API_KEY"] = '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'
        
    openai.api_key = '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'

    def generate_email(self, userPrompt ="Rédige moi une lettre", start=""):
        """Renvoie une lettre générée en utilisant l'intelligence artificielle"""

        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=userPrompt + "\n\n" + start,
        temperature=0.71,
        max_tokens=2049,
        top_p=1,
        frequency_penalty=0.36,
        presence_penalty=0.75
        )
        return response.get("choices")[0]['text']

    def replace_spaces_with_pluses(self, sample):
        """Renvoie une chaîne de caractères avec chaque espace remplacé par un plus afin que le lien d'email puisse être formaté correctement"""
        changed = list(sample)
        for i, c in enumerate(changed):
            if(c == ' ' or c =='  ' or c =='   ' or c=='\n' or c=='\n\n'):
                changed[i] = '+'
        return ''.join(changed)
