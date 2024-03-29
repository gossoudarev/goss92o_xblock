"""This XBlock by Goss allows to send data for automatic check and grade the result."""

import pkg_resources
from web_fragments.fragment import Fragment

from xblock.core import XBlock
from xblock.scorable import ScorableXBlockMixin, Score


from xblock.fields import Integer, Scope, UNSET
from django.utils.safestring import SafeText
import textwrap
import json
import sys
import random

if sys.version_info.major >= 3:
    from urllib.request import urlopen
else:
    from urllib import urlopen


@XBlock.wants('user')
class Goss92XBlock(ScorableXBlockMixin, XBlock):
    """
    XBlock checks if a certain URL returns what is expected
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.
    #package = __package__
    always_recalculate_grades = True

    score2 = Integer(
        default=0, scope=Scope.user_state,
        help="An indicator of success",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def has_submitted_answer(self):
        """
        Returns True if the user has made a submission.
        """
        return self.fields['score2'].is_set_on(self)


    def max_score(self):  # pylint: disable=no-self-use
        """
        Return the problem's max score
        Required by the grading system in the LMS.
        """
        return 1

    def set_score(self, score):
        """
        Sets the score on this block.
        Takes a Score namedtuple containing a raw
        score and possible max (for this block, we expect that this will
        always be 1).
        """
        #assert score.raw_possible == self.max_score()
        #score.raw_earned = 1/2
        self.score2 = 1 #score.raw_earned

    def get_score(self):
        """
        Return the problem's current score as raw values.
        """

        return Score(1, self.max_score())


    def calculate_score(self):
        """
        Returns a newly-calculated raw score on the problem for the learner
        based on the learner's current state.
        """
        return Score(1, self.max_score())

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view, shown to students
        when viewing courses.
        """
        user_service = self.runtime.service(self, 'user')
        xb_user = user_service.get_current_user()
        CURRENT = xb_user.opt_attrs.get('edx-platform.username')

        html = self.resource_string("static/html/gossxblock.html")
        frag = Fragment(html.format(self=self))

        res0 = textwrap.dedent("""
            <p id='goss_hidden'><span id="gosscurrent">{}</span></p>
        """).format(CURRENT)
        frag.add_content(SafeText(res0))

        HTMLURL = 'https://node-server.online/r/assets/x92.html'
        if sys.version_info.major >= 3:
            response = urlopen(HTMLURL)
            encoding = response.info().get_content_charset('utf-8')
            html_data = response.read().decode(encoding)
        else:
            html_data = urlopen(HTMLURL).read().decode('utf-8')

        res = textwrap.dedent(html_data)
        frag.add_content(SafeText(res))

        # course = store.get_course(self.location.course_key)
        vertical = self.get_parent()
        sequential = vertical.get_parent()
        chapter = sequential.get_parent()

        context = {
            'vertical_name': vertical.display_name,
            'sequential_name': sequential.display_name,
            'chapter_name': chapter.display_name,
        }

        frag.add_css(self.resource_string("static/css/gossxblock.css"))
        frag.add_javascript(self.resource_string("static/js/src/goss92xblock.js"))
        frag.initialize_js('Goss92XBlock', context)
        return frag


    @XBlock.json_handler
    def set_score2(self, data, suffix=''):
        """
        An example handler, which increments the data.
        """
        # indicator is now 100...
        if data['key'] == 'hundred':
             self.score2 = 1
        else:
             self.score2 = 0



        self._publish_grade(Score(self.score2, self.max_score()))


        return {"score": self.score2}


    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("goss92XBlock",
             """<problem/>
             """),
            ("Multiple goss92XBlock",
             """<vertical_demo>
                <goss92xblock/>
                <goss92xblock/>
                <goss92xblock/>
                </vertical_demo>
             """),
        ]
