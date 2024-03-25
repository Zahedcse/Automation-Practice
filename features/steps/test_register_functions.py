from behave import *

use_step_matcher("re")


@When('Navigate to url')
def step_impl(context, ):
    context.app.reg_page.NavigateToURL()
    raise NotImplementedError(u'STEP: When Navigate to url ')
