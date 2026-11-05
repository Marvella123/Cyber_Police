import unittest

from cyber_police_core import static_text_signals, static_url_signals


class StaticSignalTests(unittest.TestCase):
    def test_security_notifications_disable_instruction_is_flagged(self):
        result = static_text_signals(
            "The new version works better if you disable those annoying security notifications first."
        )
        self.assertTrue(any("disable security notifications" in item for item in result))

    def test_authorised_maintenance_pause_is_not_automatically_flagged(self):
        result = static_text_signals(
            "Security notifications may briefly pause while the authorised update runs. "
            "Do not change your antivirus or firewall settings yourself."
        )
        self.assertEqual(result, [])

    def test_joke_framing_is_context_not_proof(self):
        result = static_text_signals("Don't take this too seriously; it's just for laughs.")
        self.assertTrue(any("can be innocent" in item for item in result))

    def test_subdomain_of_reserved_example_domain_is_marked(self):
        _, findings = static_url_signals(
            "http://login-microsoft-security.example.com/account/verify?session=84921"
        )
        joined = " ".join(note for item in findings for note in item["observations"]).lower()
        self.assertIn("reserved", joined)
        self.assertIn("http", joined)


if __name__ == "__main__":
    unittest.main()
