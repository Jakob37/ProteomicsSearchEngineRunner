PARAMS_TEMPLATE = """
database_name = {database}
num_threads = {threads}                        # 0=poll CPU to set num threads; else specify num threads directly (max 64)

precursor_mass_tolerance = {precursor_mass_tolerance}
precursor_mass_units = {precursor_mass_units_int}               # 0=Daltons, 1=ppm
precursor_true_tolerance = {precursor_true_tolerance}
precursor_true_units = {precursor_true_units_int}               # 0=Daltons, 1=ppm
fragment_mass_tolerance = {fragment_mass_tolerance}
fragment_mass_units = {fragment_mass_units_int}		           # 0=Daltons, 1=ppm

isotope_error = 0                      # 0=off, 0/1/2 (standard C13 error)

search_enzyme_name = Trypsin
search_enzyme_cutafter = KR
search_enzyme_butnotafter = P

num_enzyme_termini = 2                 # 2 for enzymatic, 1 for semi-enzymatic, 0 for nonspecific digestion
allowed_missed_cleavage = 1            # maximum value is 5

clip_nTerm_M = 1

#maximum of 7 mods - amino acid codes, * for any amino acid, [ and ] specifies protein termini, n and c specifies peptide termini
variable_mod_01 = 15.9949 M
variable_mod_02 = 42.0106 [*
#variable_mod_03 = 79.96633 STY
#variable_mod_03 = -17.0265 nQnC
#variable_mod_04 = -18.0106 nE

allow_multiple_variable_mods_on_residue = 1  	# static mods are not considered
max_variable_mods_per_mod = 3 			        # maximum of 5
max_variable_mods_combinations = 1000  		    # maximum of 65534, limits number of modified peptides generated from sequence

output_file_extension = pepXML	       #pepXML
output_format = pepXML				   #pepXML or tsv
output_report_topN = 1
output_max_expect = 50

precursor_charge = {min_charge} {max_charge}                 # precursor charge range to analyze; does not override any existing charge; 0 as 1st entry ignores parameter
override_charge = 0                    # 0=no, 1=yes to override existing precursor charge states with precursor_charge parameter

digest_min_length = 7
digest_max_length = 50
digest_mass_range = 500.0 5000.0       # MH+ peptide mass range to analyze
max_fragment_charge = 2                # set maximum fragment charge state to analyze (allowed max 5)

#open search parameters
track_zero_topN = 0		           # in addition to topN results, keep track of top results in zero bin
zero_bin_accept_expect = 0	       # boost top zero bin entry to top if it has expect under 0.01 - set to 0 to disable
zero_bin_mult_expect = 1	       # disabled if above passes - multiply expect of zero bin for ordering purposes (does not affect reported expect)
add_topN_complementary = 0

# spectral processing

minimum_peaks = 15                   # required minimum number of peaks in spectrum to search (default 10)
use_topN_peaks = 100
min_fragments_modelling = 3
min_matched_fragments = 6
minimum_ratio = 0.01		         # filter peaks below this fraction of strongest peak
clear_mz_range = 0.0 0.0             # for iTRAQ/TMT type data; will clear out all peaks in the specified m/z range

# additional modifications

add_Cterm_peptide = 0.0
add_Nterm_peptide = 0.0
add_Cterm_protein = 0.0
add_Nterm_protein = 0.0

add_G_glycine = 0.0000                 # added to G - avg.  57.0513, mono.  57.02146
add_A_alanine = 0.0000                 # added to A - avg.  71.0779, mono.  71.03711
add_S_serine = 0.0000                  # added to S - avg.  87.0773, mono.  87.03203
add_P_proline = 0.0000                 # added to P - avg.  97.1152, mono.  97.05276
add_V_valine = 0.0000                  # added to V - avg.  99.1311, mono.  99.06841
add_T_threonine = 0.0000               # added to T - avg. 101.1038, mono. 101.04768
add_C_cysteine = 57.021464             # added to C - avg. 103.1429, mono. 103.00918
add_L_leucine = 0.0000                 # added to L - avg. 113.1576, mono. 113.08406
add_I_isoleucine = 0.0000              # added to I - avg. 113.1576, mono. 113.08406
add_N_asparagine = 0.0000              # added to N - avg. 114.1026, mono. 114.04293
add_D_aspartic_acid = 0.0000           # added to D - avg. 115.0874, mono. 115.02694
add_Q_glutamine = 0.0000               # added to Q - avg. 128.1292, mono. 128.05858
add_K_lysine = 0.0000                  # added to K - avg. 128.1723, mono. 128.09496
add_E_glutamic_acid = 0.0000           # added to E - avg. 129.1140, mono. 129.04259
add_M_methionine = 0.0000              # added to M - avg. 131.1961, mono. 131.04048
add_H_histidine = 0.0000               # added to H - avg. 137.1393, mono. 137.05891
add_F_phenylalanine = 0.0000           # added to F - avg. 147.1739, mono. 147.06841
add_R_arginine = 0.0000                # added to R - avg. 156.1857, mono. 156.10111
add_Y_tyrosine = 0.0000                # added to Y - avg. 163.0633, mono. 163.06333
add_W_tryptophan = 0.0000              # added to W - avg. 186.0793, mono. 186.07931
add_B_user_amino_acid = 0.0000         # added to B - avg.   0.0000, mono.   0.00000
add_J_user_amino_acid = 0.0000         # added to J - avg.   0.0000, mono.   0.00000
add_O_user_amino_acid = 0.0000         # added to O - avg.   0.0000, mono    0.00000
add_U_user_amino_acid = 0.0000         # added to U - avg.   0.0000, mono.   0.00000
add_X_user_amino_acid = 0.0000         # added to X - avg.   0.0000, mono.   0.00000
add_Z_user_amino_acid = 0.0000         # added to Z - avg.   0.0000, mono.   0.00000
"""