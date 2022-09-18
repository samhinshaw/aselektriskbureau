import pjsua as pj


class SipTelephoneHandler(pj.CallCallback):
    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    def on_state(self):
        print(f"Call is {self.call.info().state_text}")
        print(f"Last code = {self.call.info().last_code}")
        print(f"Last reason = {self.call.info().last_reason}")

    def on_media_state(self):
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            call_slot = self.call.info().conf_slot
            global TDaemon
            TDaemon.SipClient.pjlib.conf_connect(call_slot, 0)
            self.pjlib.conf_connect(0, call_slot)
