def fCmsDarkSusyAcceptance_LinearFit_2012_8TeV(ctau_mm, mGammaD_GeV, isLxy = "noLxy"):
  if isLxy == "noLxy":
    return fCmsDarkSusyAcceptance_LinearFit_2012_8TeV_noLxy(ctau_mm, mGammaD_GeV)[0]
  elif isLxy == "Lxy44":
    return fCmsDarkSusyAcceptance_LinearFit_2012_8TeV_Lxy44(ctau_mm, mGammaD_GeV)[0]
  else:
    raise Exception, "Unknown isLxy = %s" % isLxy

def fCmsDarkSusyAcceptanceUnct_LinearFit_2012_8TeV(ctau_mm, mGammaD_GeV):
  if isLxy == "noLxy":
    return fCmsDarkSusyAcceptance_LinearFit_2012_8TeV_noLxy(ctau_mm, mGammaD_GeV)[1]
  elif isLxy == "Lxy44":
    return fCmsDarkSusyAcceptance_LinearFit_2012_8TeV_Lxy44(ctau_mm, mGammaD_GeV)[1]
  else:
    raise Exception, "Unknown isLxy = %s" % isLxy

def fCmsDarkSusyAcceptance_LinearFitToArray_2012_8TeV(ctau_mm, mGammaD_GeV, AcceptanceFromMC):
    
    mGammaD_GeV_min = 0.25
    mGammaD_GeV_max = 1.00
    
    ctau_mm_min = 0.0
    ctau_mm_max = 5.0
    
    if mGammaD_GeV < mGammaD_GeV_min or mGammaD_GeV > mGammaD_GeV_max: raise Exception, "mGammaD_GeV = %g" % mGammaD_GeV
    if ctau_mm < ctau_mm_min or ctau_mm > ctau_mm_max: raise Exception, "ctau_mm = %g" % ctau_mm

    for mlow, mhigh in [ (0.25,0.4), (0.4,0.55), (0.55,0.7), (0.7,0.85), (0.85,1.0) ]:
        for ctaulow, ctauhigh in [ (0.0,0.2), (0.2,0.5), (0.5,2.), (2.,5.) ]:
            if ctaulow <= ctau_mm <= ctauhigh and mlow <= mGammaD_GeV <= mhigh:
                break
        if ctaulow <= ctau_mm <= ctauhigh and mlow <= mGammaD_GeV <= mhigh:
            break

    ctauinc = (ctau_mm - ctaulow)/(ctauhigh - ctaulow)
    minc = (mGammaD_GeV - mlow)/(mhigh - mlow)
    
    Acceptance_LinearFit = (1. - ctauinc)*(1. - minc)*AcceptanceFromMC[ctaulow, mlow][0] + (ctauinc)*(1. - minc)*AcceptanceFromMC[ctauhigh, mlow][0] + (ctauinc)*(minc)*AcceptanceFromMC[ctauhigh, mhigh][0] + (1. - ctauinc)*(minc)*AcceptanceFromMC[ctaulow, mhigh][0]
    
    AcceptanceUncert_LinearFit = (1. - ctauinc)*(1. - minc)*AcceptanceFromMC[ctaulow, mlow][1] + (ctauinc)*(1. - minc)*AcceptanceFromMC[ctauhigh, mlow][1] + (ctauinc)*(minc)*AcceptanceFromMC[ctauhigh, mhigh][1] + (1. - ctauinc)*(minc)*AcceptanceFromMC[ctaulow, mhigh][1]
    
    return Acceptance_LinearFit, AcceptanceUncert_LinearFit

################################################################################
#             2012 data 8 TeV Regular analysis cuts, no cut on Lxy              
################################################################################

# (ctau in mm, mGammaD in GeV) : (acceptance)
CmsDarkSusyAcceptance_PointsFromMC_2012_8TeV_noLxy = {
(	0.00	,	0.25	): (	0.10077	,	0.00106	),
(	0.20	,	0.25	): (	0.08505	,	0.00099	),
(	0.50	,	0.25	): (	0.05429	,	0.00080	),
(	2.00	,	0.25	): (	0.01119	,	0.00037	),
(	5.00	,	0.25	): (	0.00259	,	0.00018	),
(	0.00	,	0.40	): (	0.06800	,	0.00089	),
(	0.20	,	0.40	): (	0.06744	,	0.00089	),
(	0.50	,	0.40	): (	0.04872	,	0.00076	),
(	2.00	,	0.40	): (	0.01467	,	0.00043	),
(	5.00	,	0.40	): (	0.00380	,	0.00022	),
(	0.00	,	0.55	): (	0.06800	,	0.00089	),
(	0.20	,	0.55	): (	0.06480	,	0.00088	),
(	0.50	,	0.55	): (	0.05354	,	0.00080	),
(	2.00	,	0.55	): (	0.01736	,	0.00046	),
(	5.00	,	0.55	): (	0.00481	,	0.00025	),
(	0.00	,	0.70	): (	0.06800	,	0.00089	),
(	0.20	,	0.70	): (	0.06454	,	0.00090	),
(	0.50	,	0.70	): (	0.05757	,	0.00083	),
(	2.00	,	0.70	): (	0.02154	,	0.00051	),
(	5.00	,	0.70	): (	0.00671	,	0.00029	),
(	0.00	,	0.85	): (	0.06800	,	0.00089	),
(	0.20	,	0.85	): (	0.06455	,	0.00087	),
(	0.50	,	0.85	): (	0.05996	,	0.00084	),
(	2.00	,	0.85	): (	0.02581	,	0.00056	),
(	5.00	,	0.85	): (	0.00878	,	0.00033	),
(	0.00	,	1.00	): (	0.06800	,	0.00089	),
(	0.20	,	1.00	): (	0.06450	,	0.00087	),
(	0.50	,	1.00	): (	0.06099	,	0.00086	),
(	2.00	,	1.00	): (	0.02961	,	0.00060	),
(	5.00	,	1.00	): (	0.01015	,	0.00035	),

}

def fCmsDarkSusyAcceptance_LinearFit_2012_8TeV_noLxy(ctau_mm, mGammaD_GeV):
  return fCmsDarkSusyAcceptance_LinearFitToArray_2012_8TeV(ctau_mm, mGammaD_GeV, CmsDarkSusyAcceptance_PointsFromMC_2012_8TeV_noLxy)

################################################################################
#             2012 data 8 TeV Regular analysis cuts, cut on Lxy < 4.4 cm        
################################################################################

# (ctau in mm, mGammaD in GeV) : (acceptance)
CmsDarkSusyAcceptance_PointsFromMC_2012_8TeV_Lxy44 = {
(	0.00	,	0.25	): (	0.0526	),
(	0.20	,	0.25	): (	0.0393	),
(	0.50	,	0.25	): (	0.0173	),
(	2.00	,	0.25	): (	0.0021	),
(	0.00	,	0.40	): (	0.0680	),
(	0.20	,	0.40	): (	0.0508	),
(	0.50	,	0.40	): (	0.0223	),
(	2.00	,	0.40	): (	0.0027	),
(	0.00	,	0.55	): (	0.0944	),
(	0.20	,	0.55	): (	0.0705	),
(	0.50	,	0.55	): (	0.0310	),
(	2.00	,	0.55	): (	0.0038	),
(	0.00	,	0.70	): (	0.1145	),
(	0.20	,	0.70	): (	0.0855	),
(	0.50	,	0.70	): (	0.0376	),
(	2.00	,	0.70	): (	0.0046	),
(	0.00	,	0.85	): (	0.1299	),
(	0.20	,	0.85	): (	0.0970	),
(	0.50	,	0.85	): (	0.0426	),
(	2.00	,	0.85	): (	0.0052	),
(	0.00	,	1.00	): (	0.1404	),
(	0.20	,	1.00	): (	0.1048	),
(	0.50	,	1.00	): (	0.0461	),
(	2.00	,	1.00	): (	0.0057	),
}

def fCmsDarkSusyAcceptance_LinearFit_2012_8TeV_Lxy44(ctau_mm, mGammaD_GeV):
  return fCmsDarkSusyAcceptance_LinearFitToArray_2012_8TeV(ctau_mm, mGammaD_GeV, CmsDarkSusyAcceptance_PointsFromMC_2012_8TeV_Lxy44)

################################################################################
#                Functions to model acceptance w.r.t. ctau                      
################################################################################



