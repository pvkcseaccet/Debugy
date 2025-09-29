from crewai import Crew, Process
from tasks import *
from agents import *

crew = Crew(agents=[ticket_summarizer,
                    log_digger,
                    code_debugger,
                    sw_debug_engineer],
            tasks=[summarize_ticket,
                   search_logs,
                   search_code,
                   make_decision],
            process=Process.sequential)

def __main__() :
    solution = crew.kickoff()
    print(solution)

if __name__ == __main__():
    __main__()