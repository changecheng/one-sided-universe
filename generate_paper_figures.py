import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D, proj3d
import numpy as np

# Set style for academic publication
plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12.5,
    'xtick.labelsize': 9,
    'ytick.labelsize': 9,
    'legend.fontsize': 9,
    'figure.titlesize': 14
})

class Arrow3D(FancyArrowPatch):
    """
    3D Arrow with genuine solid, filled triangular arrowhead that never truncates.
    """
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.get_proj())
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)

fig = plt.figure(figsize=(16.5, 5.2), dpi=300)

# =========================================================================
# Panel (a): Standard Inflation (Aligned to Panel b structure)
# =========================================================================
ax1 = fig.add_subplot(1, 3, 1)
ax1.set_title(r"$\mathbf{(a)\ Standard\ Inflation}$", pad=15, fontsize=12, fontweight='bold')
ax1.set_xlim(-2.6, 2.6)
ax1.set_ylim(-2.6, 2.6)
ax1.axis('off')

# Left margin: Time Axis
ax1.annotate("", xy=(-2.2, 2.3), xytext=(-2.2, 0.25),
             arrowprops=dict(arrowstyle="-|>", color='#1976d2', lw=2.0, mutation_scale=15))
ax1.text(-2.2, 2.45, r"$\mathrm{Time}\ t$", ha='center', va='bottom', color='#0d47a1', fontweight='bold', fontsize=9.5)

# Inflationary bell profile (y in [0.06, 2.2])
y_top = np.linspace(0.06, 2.2, 60)
x_right = 0.26 + 0.15 * y_top + 0.25 * np.exp(y_top * 0.95) * 0.15
x_left = -x_right
ax1.fill_betweenx(y_top, x_left, x_right, color='#e3f2fd', alpha=0.8, edgecolor='#1976d2', linewidth=1.6)

# Inflation band
ax1.fill_betweenx([0.35, 1.00], [-1.5, -1.5], [1.5, 1.5], color='#fff9c4', alpha=0.65, zorder=2)
ax1.axhline(0.35, color='#fbc02d', linestyle=':', linewidth=1.0)
ax1.axhline(1.00, color='#fbc02d', linestyle=':', linewidth=1.0)

# Text cards in upper bell
ax1.text(0, 0.68, r"$\mathbf{Cosmic\ Inflation}$" + "\n" + r"($\sim e^{60}\ \mathrm{expansion}$)", 
         ha='center', va='center', fontsize=9.0, color='#e65100', fontweight='bold', zorder=5,
         bbox=dict(boxstyle="round,pad=0.32", facecolor="#fffde7", edgecolor="#f57f17", alpha=0.95, lw=1.1))

ax1.text(0, 1.65, r"$\mathbf{Observable\ Universe}$" + "\n" + r"($\Lambda\mathrm{CDM}\ \mathrm{era}$)", 
         ha='center', va='center', fontsize=9.2, color='#0d47a1', fontweight='bold', zorder=5,
         bbox=dict(boxstyle="round,pad=0.32", facecolor="#ffffff", edgecolor="#1565c0", alpha=0.95, lw=1.1))

# Singularity dot at center (0, 0)
ax1.scatter([0], [0], color='#d32f2f', s=140, zorder=6, edgecolors='black', linewidth=1.2)

# Curvature Singularity card at y = -1.25
ax1.annotate("", xy=(0, -0.85), xytext=(0, -0.15),
             arrowprops=dict(arrowstyle="-|>", color='#d32f2f', lw=1.5, linestyle="--", mutation_scale=12))
ax1.text(0, -1.25, r"$\mathbf{Curvature\ Singularity}$" + "\n" + r"$t=0,\ a(0)=0\ \mathrm{(Incomplete)}$", 
         ha='center', va='center', color='#b71c1c', fontweight='bold', fontsize=8.8, zorder=5,
         bbox=dict(boxstyle="round,pad=0.32", facecolor="#ffebee", edgecolor="#d32f2f", alpha=0.95, lw=1.1))

# Sub-caption
ax1.text(0, -2.40, r"$\mathrm{Singular\ Past\ Boundary:\ Multiverse\ Liability}$", 
         ha='center', fontsize=8.8, fontstyle='italic', color='#546e7a')


# =========================================================================
# Panel (b): Boyle-Turok Mirror Universe
# =========================================================================
ax2 = fig.add_subplot(1, 3, 2)
ax2.set_title(r"$\mathbf{(b)\ Boyle\text{--}Turok\ Mirror\ Universe}$", pad=15, fontsize=12, fontweight='bold')
ax2.set_xlim(-2.6, 2.6)
ax2.set_ylim(-2.6, 2.6)
ax2.axis('off')

# Left margin: Time axes
ax2.annotate("", xy=(-2.2, 2.3), xytext=(-2.2, 0.25),
             arrowprops=dict(arrowstyle="-|>", color='#1b5e20', lw=2.0, mutation_scale=15))
ax2.text(-2.2, 2.45, r"$+t$", ha='center', va='bottom', color='#1b5e20', fontweight='bold', fontsize=10)

ax2.annotate("", xy=(-2.2, -2.3), xytext=(-2.2, -0.25),
             arrowprops=dict(arrowstyle="-|>", color='#880e4f', lw=2.0, mutation_scale=15))
ax2.text(-2.2, -2.45, r"$-t$", ha='center', va='top', color='#880e4f', fontweight='bold', fontsize=10)

# Post-bang sheet (+t)
y_top_b = np.linspace(0.06, 2.2, 50)
x_t_right = 0.35 + 0.65 * y_top_b
ax2.fill_betweenx(y_top_b, -x_t_right, x_t_right, color='#e8f5e9', alpha=0.8, edgecolor='#388e3c', linewidth=1.6)

ax2.text(0, 1.25, r"$\mathbf{Post\text{-}Bang\ Universe}$" + "\n" + r"(Matter $\psi_R$, $+t$)", 
         ha='center', va='center', fontsize=9.2, color='#1b5e20', fontweight='bold', zorder=5,
         bbox=dict(boxstyle="round,pad=0.35", facecolor="#ffffff", edgecolor="#2e7d32", alpha=0.95, lw=1.1))

# Pre-bang sheet (-t)
y_bot_b = np.linspace(-2.2, -0.06, 50)
x_b_right = 0.35 - 0.65 * y_bot_b
ax2.fill_betweenx(y_bot_b, -x_b_right, x_b_right, color='#fce4ec', alpha=0.8, edgecolor='#c2185b', linewidth=1.6)

ax2.text(0, -1.25, r"$\mathbf{Pre\text{-}Bang\ Anti\text{-}Universe}$" + "\n" + r"(Antimatter $\psi_L$, $-t$)", 
         ha='center', va='center', fontsize=9.2, color='#880e4f', fontweight='bold', zorder=5,
         bbox=dict(boxstyle="round,pad=0.35", facecolor="#ffffff", edgecolor="#c2185b", alpha=0.95, lw=1.1))

# CPT Mirror boundary
ax2.axhline(0, color='#d32f2f', linestyle='--', linewidth=2.2, zorder=4)
ax2.text(0, 0, r"$\mathbf{CPT\ Mirror\ Boundary}\ (\tau = 0)$", ha='center', va='center', 
         color='#b71c1c', fontweight='bold', fontsize=8.8, zorder=6,
         bbox=dict(boxstyle="round,pad=0.25", facecolor="#ffebee", edgecolor="#d32f2f", alpha=0.95, lw=1.0))

# Sub-caption
ax2.text(0, -2.40, r"$\mathrm{Ontological\ Duality:\ Two\ Disjoint\ Sheets}$", 
         ha='center', fontsize=8.8, fontstyle='italic', color='#546e7a')


# =========================================================================
# Panel (c): One-Sided Möbius Spacetime (Arrow3D Solid Filled Arrowheads)
# =========================================================================
ax3 = fig.add_subplot(1, 3, 3, projection='3d')
ax3.set_title(r"$\mathbf{(c)\ One\text{--}Sided\ M\ddot{o}bius\ Spacetime\ (This\ Work)}$", pad=15, fontsize=12, fontweight='bold')

# Generate 3D Möbius Strip
u = np.linspace(0, 2 * np.pi, 120)
v = np.linspace(-0.55, 0.55, 25)
u_grid, v_grid = np.meshgrid(u, v)

R = 1.65
x_mob = (R + v_grid * np.cos(u_grid / 2.0)) * np.cos(u_grid)
y_mob = (R + v_grid * np.cos(u_grid / 2.0)) * np.sin(u_grid)
z_mob = v_grid * np.sin(u_grid / 2.0)

# Layer 1: Translucent, sleek Möbius surface
surf = ax3.plot_surface(x_mob, y_mob, z_mob, cmap='Purples', alpha=0.42,
                        edgecolor='#7b1fa2', linewidth=0.15, shade=True, antialiased=True, zorder=2)

# Layer 2: Central line (conformal time tau trajectory - GOLD LOOP)
u_center = np.linspace(0, 2 * np.pi, 120)
x_c = R * np.cos(u_center)
y_c = R * np.sin(u_center)
z_c = np.zeros_like(u_center)
ax3.plot(x_c, y_c, z_c, color='#ff6f00', linewidth=3.0, linestyle='-', zorder=5)

# Layer 3: Conformal Throat (bounce line at u = 0 across strip)
v_throat = np.linspace(-0.55, 0.55, 25)
x_th = (R + v_throat)
y_th = np.zeros_like(v_throat)
z_th = np.zeros_like(v_throat)
ax3.plot(x_th, y_th, z_th, color='#d50000', linewidth=4.0, zorder=8)

# Positions for Matter (+t) and Antimatter (-t) on the orange line
u1 = np.pi / 3.0
pos1 = np.array([R * np.cos(u1), R * np.sin(u1), 0.0])
# Upward normal vector (length 0.85)
n1 = np.array([-0.25, -0.433, 0.866]) * 0.85

u2 = 5 * np.pi / 3.0
pos2 = np.array([R * np.cos(u2), R * np.sin(u2), 0.0])
# Downward normal vector after 180° Möbius inversion (elongated to 1.22 for visual prominence)
n2 = np.array([-0.25, 0.433, -0.866]) * 1.22

pos_throat = np.array([R, 0.0, 0.0])
pos_time_left = np.array([-R, 0.0, 0.0])

# Layer 4: TRUE SOLID 3D ARROWS (Arrow3D with filled, complete triangular heads!)
arrow_green = Arrow3D([pos1[0], pos1[0]+n1[0]], [pos1[1], pos1[1]+n1[1]], [pos1[2], pos1[2]+n1[2]],
                      mutation_scale=22, lw=3.2, arrowstyle='-|>', color='#00c853', zorder=50)
ax3.add_artist(arrow_green)

arrow_red = Arrow3D([pos2[0], pos2[0]+n2[0]], [pos2[1], pos2[1]+n2[1]], [pos2[2], pos2[2]+n2[2]],
                    mutation_scale=22, lw=3.2, arrowstyle='-|>', color='#d50000', zorder=50)
ax3.add_artist(arrow_red)

# Layer 5: Prominent Anchor Beads (Rooted on orange track, zorder=60)
ax3.scatter([pos1[0]], [pos1[1]], [pos1[2]], color='#00c853', s=85, edgecolors='black', linewidth=1.6, zorder=60)
ax3.scatter([pos2[0]], [pos2[1]], [pos2[2]], color='#d50000', s=85, edgecolors='black', linewidth=1.6, zorder=60)
ax3.scatter([pos_throat[0]], [pos_throat[1]], [pos_throat[2]], color='#d50000', s=85, edgecolors='black', linewidth=1.6, zorder=60)
ax3.scatter([pos_time_left[0]], [pos_time_left[1]], [pos_time_left[2]], color='#ff6f00', s=85, edgecolors='black', linewidth=1.6, zorder=60)

# Setup camera view
ax3.set_xlim(-2.3, 2.3)
ax3.set_ylim(-2.3, 2.3)
ax3.set_zlim(-1.5, 1.5)
ax3.view_init(elev=28, azim=-60)
ax3.set_axis_off()

# Force canvas draw to compute 3D-to-2D projection
fig.canvas.draw()

def get_2d_axes_coord(pt3d):
    """Projects a 3D point to 2D normalized axes coordinates [0, 1]"""
    x2, y2, _ = proj3d.proj_transform(pt3d[0], pt3d[1], pt3d[2], ax3.get_proj())
    disp = ax3.transData.transform((x2, y2))
    return ax3.transAxes.inverted().transform(disp)

pt_psiR = get_2d_axes_coord(pos1 + n1 * 0.95)
pt_psiL = get_2d_axes_coord(pos2 + n2 * 0.95)
pt_throat = get_2d_axes_coord(pos_throat)
pt_time = get_2d_axes_coord(pos_time_left)

# -------------------------------------------------------------------------
# 2D BORDER CARDS WITH SHORT ELEGANT LEADER LINES
# -------------------------------------------------------------------------

# 1. Top-Left Card: Time Flow
ax3.annotate(r"$\mathbf{Conformal\ Time\ \tau}$" + "\n" + r"$\mathrm{Continuous\ single\ loop}$",
             xy=(pt_time[0], pt_time[1]), xycoords='axes fraction',
             xytext=(0.20, 0.80), textcoords='axes fraction',
             ha='center', va='center',
             color='#bf360c', fontsize=8.8, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.30", facecolor="#fff8e1", edgecolor="#ff6f00", alpha=0.95, lw=1.1),
             arrowprops=dict(arrowstyle="-|>", color="#ff6f00", lw=1.3, linestyle="--", connectionstyle="arc3,rad=-0.12"))

# 2. Top-Right Card: Matter Sector \psi_R (Points to green arrow)
ax3.annotate(r"$\mathbf{\psi_R\ (Matter,\ +t)}$" + "\n" + r"$\mathrm{Right\text{-}handed\ (Upward)}$",
             xy=(pt_psiR[0], pt_psiR[1]), xycoords='axes fraction',
             xytext=(0.76, 0.80), textcoords='axes fraction',
             ha='center', va='center',
             color='#1b5e20', fontsize=8.8, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.30", facecolor="#ffffff", edgecolor="#2e7d32", alpha=0.95, lw=1.1),
             arrowprops=dict(arrowstyle="-|>", color="#2e7d32", lw=1.3, linestyle="--", connectionstyle="arc3,rad=-0.12"))

# 3. Bottom-Left Card: Antimatter Sector \psi_L (Points to red arrow)
ax3.annotate(r"$\mathbf{\psi_L\ (Antimatter,\ -t)}$" + "\n" + r"$\mathrm{Left\text{-}handed\ (Downward)}$",
             xy=(pt_psiL[0], pt_psiL[1]), xycoords='axes fraction',
             xytext=(0.22, 0.22), textcoords='axes fraction',
             ha='center', va='center',
             color='#b71c1c', fontsize=8.8, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.30", facecolor="#ffffff", edgecolor="#c62828", alpha=0.95, lw=1.1),
             arrowprops=dict(arrowstyle="-|>", color="#c62828", lw=1.3, linestyle="--", connectionstyle="arc3,rad=-0.10"))

# 4. Bottom-Right Card: Conformal Throat
ax3.annotate(r"$\mathbf{Throat\ (\tau=0)}$" + "\n" + r"$CPT\ \mathbb{Z}_2\ \mathrm{Bounce}$",
             xy=(pt_throat[0], pt_throat[1]), xycoords='axes fraction',
             xytext=(0.76, 0.22), textcoords='axes fraction',
             ha='center', va='center',
             color='#b71c1c', fontsize=8.8, fontweight='bold',
             bbox=dict(boxstyle="round,pad=0.30", facecolor="#ffebee", edgecolor="#d50000", alpha=0.95, lw=1.1),
             arrowprops=dict(arrowstyle="-|>", color="#d50000", lw=1.3, linestyle="--", connectionstyle="arc3,rad=0.10"))

# 5. Sub-caption
ax3.text2D(0.50, 0.03, 
           r"$\mathrm{Single\ Non\text{-}Orientable\ 4D\ Sheet:\ }w_1(\mathcal{M}_4) \ne 0$",
           transform=ax3.transAxes, ha='center', color='#546e7a', fontsize=8.8, fontstyle='italic')

plt.tight_layout()

# Save optimized figures
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fig1_pdf = os.path.join(base_dir, "fig1_topology_comparison.pdf")
fig1_png = os.path.join(base_dir, "fig1_topology_comparison.png")

for p in [fig1_pdf, fig1_png]:
    plt.savefig(p, bbox_inches='tight', pad_inches=0.18, dpi=300)

plt.close()
print(f"Figure 1 generated successfully: {fig1_pdf}")

# ==========================================
# FIGURE 2: OBSERVATIONAL CONSTRAINTS (ns - r)
# ==========================================
from matplotlib.patches import Ellipse

fig, ax = plt.subplots(figsize=(7, 5.2), dpi=300)

# Planck 2018 + BICEP/Keck 2018 (BK18) contours
e2 = Ellipse((0.9649, 0.020), width=0.013, height=0.035, angle=25,
             color='#90caf9', alpha=0.45, label=r'Planck 2018 + BK18 ($95\%\ \mathrm{CL}$)')
e1 = Ellipse((0.9649, 0.016), width=0.008, height=0.022, angle=25,
             color='#1e88e5', alpha=0.6, label=r'Planck 2018 + BK18 ($68\%\ \mathrm{CL}$)')
ax.add_patch(e2)
ax.add_patch(e1)

# Inflation models: Starobinsky R^2 (N = 50 to 60)
N = np.linspace(50, 60, 20)
ns_staro = 1 - 2/N
r_staro = 12 / (N**2)
ax.plot(ns_staro, r_staro, color='#2e7d32', linewidth=3, label=r'Starobinsky $R^2$ Inflation ($N=50\text{--}60$)')

# Monomial phi^2 (excluded)
N_phi = np.linspace(50, 60, 20)
ns_phi = 1 - 2/N_phi
r_phi = 8 / N_phi
ax.plot(ns_phi, r_phi, color='#e53935', linestyle=':', linewidth=2.5, label=r'Monomial $\phi^2$ Inflation (Excluded)')

# LiteBIRD / CMB-S4 sensitivity threshold
ax.axhline(0.001, color='#d81b60', linestyle='--', linewidth=1.8, label=r'LiteBIRD / CMB-S4 Threshold ($r \sim 10^{-3}$)')

# THIS WORK: exact prediction point at r = 0, ns ~ 0.965
ax.scatter([0.9649], [0.0], color='#ff6f00', edgecolors='black', s=220, marker='*', zorder=10,
           label=r'$\mathbf{One\text{--}Sided\ M\ddot{o}bius\ Universe\ (This\ Work:\ } r \equiv 0\mathbf{)}$')

ax.annotate(r'$\mathbf{Primary\ Null\ Tensor\ Prediction:}\ r \equiv 0$' + '\n' + r'$n_s \approx 0.965$ (Observed Anchor)',
            xy=(0.9649, 0.001), xytext=(0.946, 0.035),
            arrowprops=dict(facecolor='#ff6f00', shrink=0.08, width=1.5, headwidth=7),
            fontsize=9.5, fontweight='bold', color='#bf360c',
            bbox=dict(boxstyle="round,pad=0.4", fc="#fff3e0", ec="#ff6f00", lw=1.2))

ax.set_xlim(0.945, 0.985)
ax.set_ylim(-0.003, 0.10)
ax.set_xlabel(r'Scalar Spectral Tilt $n_s$', fontweight='bold')
ax.set_ylabel(r'Tensor-to-Scalar Ratio $r$', fontweight='bold')
ax.set_title(r'Cosmological Parameter Constraints: $n_s$ vs. $r$', pad=12, fontweight='bold')

ax.legend(loc='upper right', frameon=True, framealpha=0.92, edgecolor='#cfd8dc')
ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout()
fig2_pdf = os.path.join(base_dir, "fig2_ns_r_constraints.pdf")
fig2_png = os.path.join(base_dir, "fig2_ns_r_constraints.png")
plt.savefig(fig2_pdf, bbox_inches='tight')
plt.savefig(fig2_png, dpi=300, bbox_inches='tight')
plt.close()
print(f"Figure 2 generated successfully: {fig2_pdf}")
