# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
         return "action_provide_information"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        topic = tracker.get_slot("topic")

        if topic == "chemistry":
            dispatcher.utter_message(text="Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions: their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances.")
        elif topic == "math":
            dispatcher.utter_message(text="Mathematics includes the study of such topics as quantity (number theory), structure (algebra), space (geometry), and change (mathematical analysis).")
        elif topic == "history":
            dispatcher.utter_message(text="History is the study of the past. Events occurring before the invention of writing systems are considered prehistory.")
        elif topic == "geography":
            dispatcher.utter_message(text="Geography is a field of science devoted to the study of the lands, features, inhabitants, and phenomena of the Earth and planets.")
        elif topic == "english":
            dispatcher.utter_message(text="English is a West Germanic language first spoken in early medieval England, which has become the leading language of international discourse in the 21st century and is currently the third most spoken native language in the world.")
        elif topic == "physics":
            dispatcher.utter_message(text="Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.")
        elif topic == "biology":
            dispatcher.utter_message(text="Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution.")
        elif topic == "computer science":
            dispatcher.utter_message(text="Computer science is the study of algorithmic processes, computational machines and computation itself.")
        elif topic == "coding":
            dispatcher.utter_message(text="Coding is the process of using a programming language to get a computer to behave how you want it to.")
        elif topic == "programming":
            dispatcher.utter_message(text="Programming is the process of creating a set of instructions that tell a computer how to perform a task.")
        elif topic == "science":
            dispatcher.utter_message(text="Science is the pursuit and application of knowledge and understanding of the natural and social world following a systematic methodology based on evidence.")
        elif topic == "technology":
            dispatcher.utter_message(text="Technology is the sum of techniques, skills, methods, and processes used in the production of goods or services or in the accomplishment of objectives, such as scientific investigation.")
        elif topic == "economics":
            dispatcher.utter_message(text="Economics is a social science concerned with the production, distribution, and consumption of goods and services.")
        elif topic == "business":
            dispatcher.utter_message(text="Business is the activity of making one's living or making money by producing or buying and selling products (such as goods and services).")
        elif topic == "finance":
            dispatcher.utter_message(text="Finance is a term for matters regarding the management, creation, and study of money and investments.")
        elif topic == "accounting":
            dispatcher.utter_message(text="Accounting is the measurement, processing, and communication of financial and non financial information about economic entities such as businesses and corporations.")
        elif topic == "marketing":
            dispatcher.utter_message(text="Marketing is the process of interesting potential customers and clients in your products and/or services.")
        elif topic == "management":
            dispatcher.utter_message(text="Management is the process of dealing with or controlling things or people.")
        elif topic == "arts":
            dispatcher.utter_message(text="The arts are a very wide range of human practices of creative expression, storytelling and cultural participation.")
        elif topic == "machine learning":
            dispatcher.utter_message(text="Machine learning is an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.")
        elif topic == "deep learning":
            dispatcher.utter_message(text="Deep learning is a subset of machine learning in artificial intelligence (AI) that has networks capable of learning unsupervised from data that is unstructured or unlabeled.")
        elif topic == "artificial intelligence":
            dispatcher.utter_message(text="Artificial intelligence (AI) is the simulation of human intelligence processes by machines, especially computer systems.")
        elif topic == "neural networks":
            dispatcher.utter_message(text="Artificial neural networks (ANN) or connectionist systems are computing systems vaguely inspired by the biological neural networks that constitute animal brains.")
        elif topic == "reinforcement learning":
            dispatcher.utter_message(text="Reinforcement learning (RL) is an area of machine learning concerned with how software agents ought to take actions in an environment in order to maximize the notion of cumulative reward.")
        elif topic == "supervised learning":
            dispatcher.utter_message(text="Supervised learning is the machine learning task of learning a function that maps an input to an output based on example input-output pairs.")
        elif topic == "unsupervised learning":
            dispatcher.utter_message(text="Unsupervised learning is a type of machine learning that looks for previously undetected patterns in a data set with no pre-existing labels and with a minimum of human supervision.")
        elif topic == "natural language processing":
            dispatcher.utter_message(text="Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence concerned with the interactions between computers and human language, in particular how to program computers to process and analyze large amounts of natural language data.")
        elif topic == "computer vision":
            dispatcher.utter_message(text="Computer vision is an interdisciplinary scientific field that deals with how computers can gain high-level understanding from digital images or videos.")
        elif topic == "data science":
            dispatcher.utter_message(text="Data science is an inter-disciplinary field that uses scientific methods, processes, algorithms and systems to extract knowledge and insights from structured and unstructured data.")
        elif topic == "big data":
            dispatcher.utter_message(text="Big data is a field that treats ways to analyze, systematically extract information from, or otherwise deal with data sets that are too large or complex to be dealt with by traditional data-processing application software.")
        elif topic == "data analytics":
            dispatcher.utter_message(text="Data analytics is the science of analyzing raw data in order to make conclusions about that information.")
        elif topic == "data engineering":
            dispatcher.utter_message(text="Data engineering is the aspect of data science that focuses on practical applications of data collection and analysis.")
        elif topic == "data warehousing":
            dispatcher.utter_message(text="Data warehousing is the electronic storage of a large amount of information by a business, in a manner that is secure, reliable, easy to retrieve, and easy to manage.")
        elif topic == "data mining":
            dispatcher.utter_message(text="Data mining is a process used by companies to turn raw data into useful information.")
        elif topic == "data visualization":
            dispatcher.utter_message(text="Data visualization is the graphical representation of information and data.")
        elif topic == "cyber security":
            dispatcher.utter_message(text="Cyber security is the practice of defending computers, servers, mobile devices, electronic systems, networks, and data from malicious attacks.")
        elif topic == "information security":
            dispatcher.utter_message(text="Information security, sometimes shortened to infosec, is the practice of protecting information by mitigating information risks.")
        elif topic == "network security":
            dispatcher.utter_message(text="Network security consists of the policies and practices adopted to prevent and monitor unauthorized access, misuse, modification, or denial of a computer network and network-accessible resources.")
        elif topic == "cloud computing":
            dispatcher.utter_message(text="Cloud computing is the on-demand availability of computer system resources, especially data storage and computing power, without direct active management by the user.")
        elif topic == "distributed system":
            dispatcher.utter_message(text="A distributed system is a system whose components are located on different networked computers, which communicate and coordinate their actions by passing messages to one another.")
        elif topic == "operating system":
            dispatcher.utter_message(text="An operating system (OS) is system software that manages computer hardware, software resources, and provides common services for computer programs.")
        elif topic == "computer network":
            dispatcher.utter_message(text="A computer network is a group of computers that use a set of common communication protocols over digital interconnections for the purpose of sharing resources located on or provided by the network nodes.")
        elif topic == "web development":
            dispatcher.utter_message(text="Web development is the work involved in developing a website for the Internet or an intranet.")
        elif topic == "mobile development":
            dispatcher.utter_message(text="Mobile app development is the act or process by which a mobile app is developed for mobile devices, such as personal digital assistants, enterprise digital assistants or mobile phones.")
        elif topic == "game development":
            dispatcher.utter_message(text="Game development is the process of creating video games.")
        elif topic == "software development":
            dispatcher.utter_message(text="Software development is the process of conceiving, specifying, designing, programming, documenting, testing, and bug fixing involved in creating and maintaining applications, frameworks, or other software components.")
        elif topic == "software engineering":
            dispatcher.utter_message(text="Software engineering is the systematic application of engineering approaches to the development of software.")
        elif topic == "agile":
            dispatcher.utter_message(text="Agile software development is an approach to software development under which requirements and solutions evolve through the collaborative effort of self-organizing and cross-functional teams and their customer(s)/end user(s).")
        elif topic == "scrum":
            dispatcher.utter_message(text="Scrum is a framework within which people can address complex adaptive problems, while productively and creatively delivering products of the highest possible value.")
        elif topic == "kanban":
            dispatcher.utter_message(text="Kanban is a method for managing knowledge work with an emphasis on just-in-time delivery while not overloading the team members.")
        else:
            dispatcher.utter_message(text="I am sorry, I do not have information on that topic. Please try another topic.")

        return []
