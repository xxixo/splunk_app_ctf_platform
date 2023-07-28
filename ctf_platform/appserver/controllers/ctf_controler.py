import splunk.appserver.mrsparkle.controllers as controllers
from splunk.appserver.mrsparkle.lib.decorators import expose_page
import datetime
import cherrypy


PATH_TO_ANSWER_LOG_FILE = f"/opt/splunk/etc/apps/ctf_platform/answers/ctf_answers.log"
PATH_TO_ANSWERS_FILE = f"/opt/splunk/etc/apps/ctf_platform/lookups/ctf_answer.csv"

class Controller(controllers.BaseController):
	@expose_page(must_login=True, methods=['GET'])
	def submit_question(self, **params):
		username = params['Username']
		question_id = params['Question_id']
		question_number = question_id[1:]
		answer = params['Answer']
		attempt = params['Attempt']
		with open(PATH_TO_ANSWERS_FILE,"r") as answers_file:
			for line in answers_file.readlines():
            	#extract right answer from list of answer
				if question_id == line.strip().split(",")[0]:
					right_answer = line.strip().split(",")[1]
			answers_file.close()
		if str(answer).lower().strip() == str(right_answer).lower().strip():
			state = "true"
		else:
			state = "false"

		formatted_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		log_line = f"data={formatted_datetime},user={username},question_id={question_id},answer_text={answer},is_correct={state},attempt={int(attempt)+1}"
		with open(PATH_TO_ANSWER_LOG_FILE, "a") as log:
			log.write(log_line)
			log.close()
		if state=="true":
                        raise cherrypy.HTTPRedirect(str('%s' % (f'/en-US/app/ctf_platform/ctf_questions')), 302)
		else:
			raise cherrypy.HTTPRedirect(str('%s' % (f'/en-US/app/ctf_platform/ctf_answer?Questiom_numer={question_number}')), 302)
