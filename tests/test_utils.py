#!/usr/bin/env python3

import unittest
from pySim import utils
from pySim.ts_31_102 import EF_SUCI_Calc_Info

class DecTestCase(unittest.TestCase):

	def testSplitHexStringToListOf5ByteEntries(self):
		input_str = "ffffff0003ffffff0002ffffff0001"
		expected = [
			"ffffff0003",
			"ffffff0002",
			"ffffff0001",
		]
		self.assertEqual(utils.hexstr_to_Nbytearr(input_str, 5), expected)

	def testDecMCCfromPLMN(self):
		self.assertEqual(utils.dec_mcc_from_plmn("92f501"), 295)

	def testDecMCCfromPLMN_unused(self):
		self.assertEqual(utils.dec_mcc_from_plmn("ff0f00"), 4095)

	def testDecMNCfromPLMN_twoDigitMNC(self):
		self.assertEqual(utils.dec_mnc_from_plmn("92f501"), 10)

	def testDecMNCfromPLMN_threeDigitMNC(self):
		self.assertEqual(utils.dec_mnc_from_plmn("031263"), 361)

	def testDecMNCfromPLMN_unused(self):
		self.assertEqual(utils.dec_mnc_from_plmn("00f0ff"), 4095)

	def test_enc_plmn(self):
		with self.subTest("2-digit MCC"):
			self.assertEqual(utils.enc_plmn("001", "01F"), "00F110")
			self.assertEqual(utils.enc_plmn("001", "01"), "00F110")
			self.assertEqual(utils.enc_plmn("295", "10"), "92F501")

		with self.subTest("3-digit MCC"):
			self.assertEqual(utils.enc_plmn("001", "001"), "001100")
			self.assertEqual(utils.enc_plmn("302", "361"), "031263")

	def testDecAct_noneSet(self):
		self.assertEqual(utils.dec_act("0000"), [])

	def testDecAct_onlyUtran(self):
		self.assertEqual(utils.dec_act("8000"), ["UTRAN"])

	def testDecAct_onlyEUtran(self):
		self.assertEqual(utils.dec_act("4000"), ["E-UTRAN"])

	def testDecAct_onlyGsm(self):
		self.assertEqual(utils.dec_act("0080"), ["GSM"])

	def testDecAct_onlyGsmCompact(self):
		self.assertEqual(utils.dec_act("0040"), ["GSM COMPACT"])

	def testDecAct_onlyCdma2000HRPD(self):
		self.assertEqual(utils.dec_act("0020"), ["cdma2000 HRPD"])

	def testDecAct_onlyCdma20001xRTT(self):
		self.assertEqual(utils.dec_act("0010"), ["cdma2000 1xRTT"])

	def testDecAct_allSet(self):
		self.assertEqual(utils.dec_act("ffff"), ["UTRAN", "E-UTRAN", "GSM", "GSM COMPACT", "cdma2000 HRPD", "cdma2000 1xRTT"])

	def testDecxPlmn_w_act(self):
		expected = {'mcc': 295, 'mnc': 10, 'act': ["UTRAN"]}
		self.assertEqual(utils.dec_xplmn_w_act("92f5018000"), expected)

	def testFormatxPlmn_w_act(self):
		input_str = "92f501800092f5508000ffffff0000ffffff0000ffffff0000ffffff0000ffffff0000ffffff0000ffffff0000ffffff0000"
		expected  = "\t92f5018000 # MCC: 295 MNC: 010 AcT: UTRAN\n"
		expected += "\t92f5508000 # MCC: 295 MNC: 005 AcT: UTRAN\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		expected += "\tffffff0000 # unused\n"
		self.assertEqual(utils.format_xplmn_w_act(input_str), expected)


	def testDecodeSuciCalcInfo(self):
		# TS31.121 4.9.4 EF_SUCI_Calc_Info test file
		testfile = "A006020101020000A14B80011B81210272DA71976234CE833A6907425867B82E074D44EF907DFB4B3E21C1C2256EBCD180011E81205A8D38864820197C3394B92613B20B91633CBD897119273BF8E4A6F4EEC0A650"
		expected = {
			'prot_scheme_id_list': [
				{'priority': 0, 'identifier': 2, 'key_index': 1},
				{'priority': 1, 'identifier': 1, 'key_index': 2},
				{'priority': 2, 'identifier': 0, 'key_index': 0}],
			'hnet_pubkey_list': [
				{'hnet_pubkey_identifier': 27, 'hnet_pubkey': '0272DA71976234CE833A6907425867B82E074D44EF907DFB4B3E21C1C2256EBCD1'.lower()}, # because h2b/b2h returns all lower-case
				{'hnet_pubkey_identifier': 30, 'hnet_pubkey': '5A8D38864820197C3394B92613B20B91633CBD897119273BF8E4A6F4EEC0A650'.lower()}]
			}
		suci_calc_info = EF_SUCI_Calc_Info()
		decoded = suci_calc_info._decode_hex(testfile)
		self.assertDictEqual(expected, decoded)

	def testEncodeSuciCalcInfo(self):
		# TS31.121 4.9.4 EF_SUCI_Calc_Info test file
		expected = "A006020101020000A14B80011B81210272DA71976234CE833A6907425867B82E074D44EF907DFB4B3E21C1C2256EBCD180011E81205A8D38864820197C3394B92613B20B91633CBD897119273BF8E4A6F4EEC0A650"

		decoded_testfile = {
			'prot_scheme_id_list': [
				{'priority': 0, 'identifier': 2, 'key_index': 1},
				{'priority': 1, 'identifier': 1, 'key_index': 2},
				{'priority': 2, 'identifier': 0, 'key_index': 0}],
			'hnet_pubkey_list': [
				{'hnet_pubkey_identifier': 27, 'hnet_pubkey': '0272DA71976234CE833A6907425867B82E074D44EF907DFB4B3E21C1C2256EBCD1'.lower()},
				{'hnet_pubkey_identifier': 30, 'hnet_pubkey': '5A8D38864820197C3394B92613B20B91633CBD897119273BF8E4A6F4EEC0A650'.lower()}]
			}
		
		suci_calc_info = EF_SUCI_Calc_Info()
		encoded = suci_calc_info._encode_hex(decoded_testfile)
		self.assertEqual(encoded.lower(), expected.lower())

if __name__ == "__main__":
	unittest.main()
