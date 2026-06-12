
        "import os\n",
        "import pandas as pd\n",
        "from siconfipy import get_annual_acc, get_budget, get_fiscal\n",
        "\n",
        "outname = 'arquivo-DCA.json'\n",
        "outdir = './SICONFI'\n",
        "\n",
        "\n",
        "if not os.path.exists(outdir):\n",
        "    os.mkdir(outdir)\n",
        "\n",
        "fullname = os.path.join(outdir, outname)\n",
        "\n",
        "\n",
        "DCA = get_annual_acc(year=2025, cod=4118402)\n",
        "\n",
        "\n",
        "data = pd.DataFrame(DCA)\n",
        "\n",
        "\n",
        "data.to_json(fullname, orient='records', force_ascii=False, indent=4)\n",
        "\n",
        "print(f\"Arquivo salvo com sucesso em: {fullname}\")\n",
        "\n",
        "outname = 'arquivo-RREO.json'\n",
        "outdir = './SICONFI'\n",
        "\n",
        "\n",
        "if not os.path.exists(outdir):\n",
        "    os.mkdir(outdir)\n",
        "\n",
        "fullname = os.path.join(outdir, outname)\n",
        "\n",
        "\n",
        "RREO = get_budget(year=2025, period =1, cod=4118402)\n",
        "\n",
        "\n",
        "data = pd.DataFrame(RREO)\n",
        "\n",
        "\n",
        "data.to_json(fullname, orient='records', force_ascii=False, indent=4)\n",
        "\n",
        "print(f\"Arquivo salvo com sucesso em: {fullname}\")\n",
        "\n",
        "outname = 'arquivo-RGF.json'  # Corrigido o erro de digitação \"arquvivo\"\n",
        "outdir = './SICONFI'\n",
        "\n",
        "\n",
        "if not os.path.exists(outdir):\n",
        "    os.mkdir(outdir)\n",
        "\n",
        "fullname = os.path.join(outdir, outname)\n",
        "\n",
        "\n",
        "RGF = get_fiscal(year=2025, period= 1, cod=4118402)\n",
        "\n",
        "\n",
        "data = pd.DataFrame(RGF)\n",
        "\n",
        "\n",
        "data.to_json(fullname, orient='records', force_ascii=False, indent=4)\n",
        "\n",
        "print(f\"Arquivo salvo com sucesso em: {fullname}\")\n",
        "\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "nWZu9aWDTVLg"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Nova seção"
      ],
      "metadata": {
        "id": "A0LBKb_lSlrY"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "TyToQuKGQjnn"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "outname = 'arquvivo-RREO.csv'\n",
        "outdir = './SICONFI'\n",
        "\n",
        "if not os.path.exists(outdir)\n",
        "    os.mkdir(outdir)\n",
        "fullname = os.patch.join(outdir, outname)\n",
        "\n",
        "\n",
        "rreo = get_budget (year = 2026, period = 1, cod = 4118402)\n",
        "data = pd.dataframe (rreo)\n",
        "data.to_csv (fullname, sep = ';' , encoding = 'UTF-1-sig')\n",
        "    "
      ],
      "metadata": {
        "id": "SXHKUM7UQwyh"
      }
    }
  ]
}
