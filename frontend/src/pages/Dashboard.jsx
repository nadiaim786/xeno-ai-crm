import { useEffect, useState } from "react";

import {
  FaRobot,
  FaChartLine,
  FaUsers,
  FaWhatsapp
} from "react-icons/fa";

import MetricCard from "../components/MetricCard";
import CampaignCard from "../components/CampaignCard";
import SectionTitle from "../components/SectionTitle";

import {
  fetchAnalytics,
  generateCampaign,
  segmentAudience
} from "../services/api";

function Dashboard() {

  const [
    analytics,
    setAnalytics
  ] = useState(null);

  const [
    segmentPrompt,
    setSegmentPrompt
  ] = useState("");

  const [
    segmentResult,
    setSegmentResult
  ] = useState(null);

  const [
    campaignGoal,
    setCampaignGoal
  ] = useState("");

  const [
    campaign,
    setCampaign
  ] = useState(null);

  const [
    loadingSegment,
    setLoadingSegment
  ] = useState(false);

  const [
    loadingCampaign,
    setLoadingCampaign
  ] = useState(false);

  useEffect(() => {
    loadAnalytics();
  }, []);

  const loadAnalytics =
    async () => {

      try {

        const response =
          await fetchAnalytics();

        setAnalytics(
          response.data
        );

      } catch (error) {

        console.log(error);
      }
    };

  const handleSegment =
    async () => {

      if (!segmentPrompt)
        return;

      setLoadingSegment(
        true
      );

      try {

        const response =
          await segmentAudience(
            segmentPrompt
          );

        setSegmentResult(
          response.data
        );

      } catch (error) {

        console.log(error);

      } finally {

        setLoadingSegment(
          false
        );
      }
    };

  const handleCampaign =
    async () => {

      if (!campaignGoal)
        return;

      setLoadingCampaign(
        true
      );

      try {

        const response =
          await generateCampaign(
            campaignGoal
          );

        setCampaign(
          response.data
        );

        loadAnalytics();

      } catch (error) {

        console.log(error);

      } finally {

        setLoadingCampaign(
          false
        );
      }
    };

  const scrollToSection =
    (sectionId) => {

      document
        .getElementById(
          sectionId
        )
        ?.scrollIntoView({
          behavior:
            "smooth",
          block:
            "start"
        });
    };

  return (

    <div className="min-h-screen bg-slate-100 flex">

      {/* Sidebar */}
      <div className="w-72 bg-slate-900 text-white p-6 sticky top-0 h-screen">

        <h1 className="text-3xl font-bold">
          XenoReach
        </h1>

        <p className="text-slate-400 mt-2">
          AI CRM Dashboard
        </p>

        <div className="mt-10 space-y-4">

          <button
            onClick={() =>
              scrollToSection(
                "analytics"
              )
            }
            className="flex items-center gap-3 bg-slate-800 hover:bg-slate-700 transition p-4 rounded-xl w-full"
          >
            <FaChartLine />
            Analytics
          </button>

          <button
            onClick={() =>
              scrollToSection(
                "segmentation"
              )
            }
            className="flex items-center gap-3 hover:bg-slate-800 transition p-4 rounded-xl w-full"
          >
            <FaUsers />
            Segmentation
          </button>

          <button
            onClick={() =>
              scrollToSection(
                "campaigns"
              )
            }
            className="flex items-center gap-3 hover:bg-slate-800 transition p-4 rounded-xl w-full"
          >
            <FaRobot />
            AI Campaigns
          </button>

          <button
            onClick={() =>
              scrollToSection(
                "channels"
              )
            }
            className="flex items-center gap-3 hover:bg-slate-800 transition p-4 rounded-xl w-full"
          >
            <FaWhatsapp />
            Channels
          </button>

        </div>

      </div>

      {/* Main Content */}
      <div className="flex-1 p-10 space-y-16">

        {/* Hero */}
        <div className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white rounded-3xl p-10 shadow-lg">

          <h1 className="text-5xl font-bold">
            XenoReach AI
          </h1>

          <p className="text-lg mt-4 opacity-90">
            AI-native CRM for shopper engagement
          </p>

        </div>

        {/* Analytics */}
        <div
          id="analytics"
          className="scroll-mt-20"
        >

          <SectionTitle
            title="Campaign Analytics"
          />

          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-5 mt-5">

            <MetricCard
              title="Sent"
              value={
                analytics?.sent || 0
              }
            />

            <MetricCard
              title="Delivered"
              value={
                analytics?.delivered || 0
              }
            />

            <MetricCard
              title="Opened"
              value={
                analytics?.opened || 0
              }
            />

            <MetricCard
              title="Clicked"
              value={
                analytics?.clicked || 0
              }
            />

            <MetricCard
              title="CTR"
              value={
                analytics?.ctr
                || "0%"
              }
            />

            <MetricCard
              title="Conversion"
              value={
                analytics
                  ?.conversion_rate
                  || "0%"
              }
            />

          </div>

        </div>

        {/* Segmentation */}
        <div
          id="segmentation"
          className="bg-white rounded-3xl p-8 shadow-sm scroll-mt-20"
        >

          <SectionTitle
            title="AI Audience Segmentation"
          />

          <textarea
            className="w-full border border-gray-300 rounded-2xl p-4 mt-4"
            rows="5"
            placeholder="Find inactive premium shoppers from Chennai"
            value={
              segmentPrompt
            }
            onChange={(e) =>
              setSegmentPrompt(
                e.target.value
              )
            }
          />

          <button
            className="bg-indigo-600 text-white px-6 py-3 rounded-xl mt-5 hover:bg-indigo-700 transition"
            onClick={
              handleSegment
            }
          >
            {
              loadingSegment
                ? "Generating..."
                : "Generate Audience"
            }
          </button>

          {
            segmentResult && (
              <div className="bg-slate-100 p-5 rounded-2xl mt-5">

                <p>
                  <strong>
                    Audience Size:
                  </strong>{" "}
                  {
                    segmentResult
                      .audience_size
                  }
                </p>

                <p className="mt-2">
                  <strong>
                    Avg Spend:
                  </strong>{" "}
                  ₹
                  {
                    segmentResult
                      .avg_spend
                  }
                </p>

                <pre className="mt-4 overflow-x-auto text-sm">
                  {
                    JSON.stringify(
                      segmentResult
                        .interpreted_filters,
                      null,
                      2
                    )
                  }
                </pre>

              </div>
            )
          }

        </div>

        {/* Campaign */}
        <div
          id="campaigns"
          className="bg-white rounded-3xl p-8 shadow-sm scroll-mt-20"
        >

          <SectionTitle
            title="AI Campaign Generator"
          />

          <textarea
            className="w-full border border-gray-300 rounded-2xl p-4 mt-4"
            rows="5"
            placeholder="Win back dormant premium shoppers"
            value={
              campaignGoal
            }
            onChange={(e) =>
              setCampaignGoal(
                e.target.value
              )
            }
          />

          <button
            className="bg-purple-600 text-white px-6 py-3 rounded-xl mt-5 hover:bg-purple-700 transition"
            onClick={
              handleCampaign
            }
          >
            {
              loadingCampaign
                ? "Generating..."
                : "Generate Campaign"
            }
          </button>

          <CampaignCard
            campaign={
              campaign
            }
          />

        </div>

        {/* Channels */}
        <div
          id="channels"
          className="bg-white rounded-3xl p-8 shadow-sm scroll-mt-20"
        >

          <SectionTitle
            title="Connected Channels"
          />

          <div className="bg-green-50 border border-green-200 p-5 rounded-2xl mt-5">

            <div className="flex items-center gap-3">

              <FaWhatsapp
                className="text-2xl text-green-600"
              />

              <div>

                <h2 className="font-bold text-lg">
                  WhatsApp
                </h2>

                <p className="text-gray-500">
                  Channel Service Connected
                </p>

              </div>

            </div>

          </div>

        </div>

      </div>

    </div>
  );
}

export default Dashboard;