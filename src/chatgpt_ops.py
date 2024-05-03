import os
from openai import OpenAI
from dotenv import load_dotenv


class ChatGPT_Proxy():

    def __init__(self):

        load_dotenv()
        api_key_map = "OPENAI_API_KEY"
        self.client = OpenAI(
            api_key = os.getenv(api_key_map),
        )


    def message_chatgpt(self, chat_history):

        chat_completion = self.client.chat.completions.create(
                messages = chat_history,
                model = "gpt-4-turbo",
            )
        response = chat_completion.choices[0].message.content
        return(response)


    def get_brand_mvv(self, brand: str):

        message = {
            "role": "user",
            "content": f"Give me a brief and concise statement on the mission, vision and values of this brand: {brand}"
        }

        chat_title = self.message_chatgpt([message])
        return(chat_title)
    

    def generate_sentiment_analysis(self, brand: str, features :list):

        
        prompt = f"""
        We are conducting sentiment analysis to identify potential brand sponsorship partners for our LGBT+ charity with {brand}. 
        """

        if "Inclusivity Driven" in features:
            prompt += f"""
            Inclusivity and Diversity Policies: Rate the {brand} inclusivity and diversity policies. Do they have established policies supporting diversity 
            and inclusivity, including explicit support for the LGBT+ community?
            """
        if "Allyship Driven" in features:
            prompt += """
            Public Support for LGBT+ Causes: Rate the company's public support for LGBT+ causes. 
            Have they made public statements, engaged in social media activity, or sponsored events that support the LGBT+ community? 
            """
        if "Reputationally Driven" in features:
            prompt += """Reputation and Public Perception: 
            Rate the company's reputation and public perception, especially within the LGBT+ community. How positively is the company perceived, and how strong is its support within 
            the LGBT+ community? 
            """

        prompt += """Please provide a score from 1 to 10 for each of the following criteria, with 10 being the highest:
        Scoring Guide:
        1-3: Little to no support for LGBT+ causes.
        4-7: Moderate support for LGBT+ causes.
        8-10: Strong support for LGBT+ causes.
        """
        print(prompt)
        message = {
            "role": "user",
            "content": prompt
        }
        sentiment_analysis = self.message_chatgpt([message])
        return(sentiment_analysis)


    def generate_email_proposal(self, brand: str, brand_mvv: str):

        prompt = f"""
        You are a Stuart Brown, the Head of Partnerships at a charity Just Like Us, 
        this is the charity's mission statement:
        Corporate partnerships 
        At Just Like Us (JLU) we join forces with businesses to tackle challenges around fostering inclusive cultures, building tighter connections with communities, finding diverse young talent, and polishing brand image with their target audience. Each partnership is custom-made, taking on anything from one-off projects to business-wide, multi-year collaborations that span a number of departments across the business. Mission and Impact We're breaking records across the board! For eight straight years, we've been teaming up with more and more schools, our current contingent totals more than 6000 (that's 72% of secondary schools in England and Wales!), all in the name of celebrating diversity and standing up for inclusivity. Mission Just Like Us is the LGBT+ young people's charity working for a world where LGBT+ young people thrive. Our mission is to empower young people to champion LGBT+ equality. Impact Our research shows that pupils in schools that communicate positive messaging about being LGBT+ have reduced panic attacks and depression, and increased wellbeing and feelings of safety at school, whether they are LGBT+ or not.
        What We Do To 
        meet the needs of our beneficiaries we run three programmes to tackle the barriers LGBT+ young people face at school and in the workplace, levelling the playing field and creating a fairer world. The UK’s annual celebration of LGBT+ inclusion in education, reaches 6,254 secondary schools and 4.2 million pupils. Our comprehensive bank of resources empowers educators to deliver inclusive lessons and events across all subjects and key stages. The impact is evident in transformed attitudes, with 78% of educators feeling better equipped to support LGBT+ pupils, and 88% noting increased visibility of LGBT+ topics within their schools. Empowering over 800 18-25 year old LGBT+ advocates so far, this programme reshapes personal narratives as well as societal perspectives. These ambassadors share their stories with 80,000 school children a year, humanising complex issues while undergoing personal and professional development. The programme not only fosters employability (86%) and community building (88%), but also enhances understanding of LGBT+ lives in schools - teachers note a 73% increase in LGBT+ acceptance!

        Write a letter to {brand} which has these mission, vision and values {brand_mvv} asking for cooperation. Focus on the common values between our charity and target brand.

        Limit the email to 300 words.
        """
        message = {
            "role": "user",
            "content": prompt
        }
        email_propsoal = self.message_chatgpt([message])
        return(email_propsoal)
    

    @staticmethod
    def get_user_payload(user_input: str) -> dict[str]:

        payload = {
            "role": "user",
            "content": user_input
        }
        return(payload)


    @staticmethod
    def get_system_payload(response) -> dict[str]:

        payload = {
            "role": "system",
            "content": response
        }
        return(payload)
