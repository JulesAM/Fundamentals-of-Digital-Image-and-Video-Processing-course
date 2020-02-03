{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled9.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyNI6GXH5ZH6NRGTzSFZ24j4",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JulesAM/Fundamentals-of-Digital-Image-and-Video-Processing-course/blob/master/autodiff-tutorial.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SHArN5PcsfZs",
        "colab_type": "code",
        "outputId": "842dcac4-5644-4cb1-ee40-a0cfac43b4d7",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 238
        }
      },
      "source": [
        "# Load Tensorflow==2.0\n",
        "try:\n",
        "    %tensorflow_version 2.x\n",
        "except Exception:\n",
        "  pass\n",
        "import tensorflow as tf\n",
        "print(tf.__version__)\n",
        "\n",
        "# input Tensor x, size(2,2) \n",
        "x = tf.ones((2, 2))\n",
        "print (\"\\n x: is a 2 x 2 Tensor with Ones\" , x)\n",
        "\n",
        "# load the Tape for recording operations\n",
        "with tf.GradientTape() as t:        # load tape for the operations on objects\n",
        "  t.watch(x)                        # records tape object\n",
        "# operation \n",
        "  y = tf.reduce_sum(x)              # y = sum along dim(tensor x) == tensor rank 0, val  = 4\n",
        "  print(\"\\ny1:\", y)\n",
        "  z = tf.multiply(y, y)             # z= y^2 \n",
        "  print(\"\\nz1:\", z)\n",
        "# To find d(z)/dx \n",
        "dz_dx = t.gradient(z, x)          # dz/dx = dz/dy * dx/dy\n",
        "print(\"\\ndz_dz:\", dz_dx)\n",
        "\n",
        "#  Value confirm\n",
        "#for i in [0, 1]:\n",
        "#  for j in [0, 1]:\n",
        "#    assert dz_dx[i][j].numpy() == 8.0\n",
        "\n",
        "#del t  # Drop the reference to the tape\n",
        "\n"
      ],
      "execution_count": 0,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "2.1.0\n",
            "\n",
            " x: is a 2 x 2 Tensor with Ones tf.Tensor(\n",
            "[[1. 1.]\n",
            " [1. 1.]], shape=(2, 2), dtype=float32)\n",
            "\n",
            "y1: tf.Tensor(4.0, shape=(), dtype=float32)\n",
            "\n",
            "z1: tf.Tensor(16.0, shape=(), dtype=float32)\n",
            "\n",
            "dz_dz: tf.Tensor(\n",
            "[[8. 8.]\n",
            " [8. 8.]], shape=(2, 2), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}